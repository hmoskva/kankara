from datetime import date, timedelta
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.utils import timezone

from customers.models import Customer
from businesses.models import Business
from products.models import Product

User = settings.AUTH_USER_MODEL


class SaleManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def this_week(self, business):
        """
            Get all this week's sales by business
        :return: queryset
        """
        date_today = date.today()
        start_week = date_today - timedelta(date.weekday(date_today) + 1)
        end_week = start_week + timedelta(7)
        return self.get_queryset().filter(
            date_created__range=[start_week,end_week]
        , business=business).order_by('-timestamp')

    def this_day(self, business):
        """
            Get all today's sales by business
        :return: queryset
        """
        return self.get_queryset().filter(date_created=date.today(), business=business)

    def total_this_week(self, business):
        """
            Get total amount received and owed for current week
            :return: dict(amount_paid__sum=amount_paid, amount_balance__sum=amt_balance)
        """
        return self.this_week(business).aggregate(Sum('amount_paid'))

    def total_today(self, business):
        """
            Get total amount received and owed for current day
            :return: dict(amount_paid__sum=amount_paid, amount_balance__sum=amt_balance)
        """
        return self.this_day(business).aggregate(Sum('amount_paid'))

    def get_number_of_purchases_for_customer_by_week(self, business, customer):
        """
            Get number of purchases by user for current week.
        :param user:
        :return:
        """
        return self.this_week(business).filter(customer=customer).count()

    def get_number_of_paid_sales_by_week(self, business):
        return self.this_week(business).filter(status='fully paid').count()

    def get_number_of_part_paid_sales_by_week(self, business):
        return self.this_week(business).filter(status='partly paid').count()

    def get_number_of_debt_sales_by_week(self, business):
        return self.this_week(business).filter(status='not paid').count()

    def get_number_of_sales_by_product(self, business, product):
        return self.this_week(business).filter(product=product).count()


class Sale(models.Model):

    STATUS_CHOICES = (
        ('fully paid', 'Fully Paid'),
        ('partly paid', 'Partly Paid'),
        ('not paid', 'Awiin'),
    )
    business = models.ForeignKey(Business, related_name='sales', null=True, blank=True)
    customer = models.ForeignKey(Customer, related_name='purchases')
    product = models.ForeignKey(Product, related_name='sales')
    units = models.IntegerField(default=1)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES)
    default_rate = models.BooleanField(default=True, verbose_name='Use fixed rate')
    amount_paid = models.IntegerField(verbose_name='Amount Paid')
    created_by = models.ForeignKey(User, related_name='created_sales')
    date_modified = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    date_created = models.DateField(auto_now_add=True)

    objects = SaleManager()

    def __str__(self):
        return 'Sale on {date} by {customer}'.format(date=str(self.date_created),
                                                     customer=self.customer.name)

    class Meta:
        ordering = ['-timestamp']

    # def save(self, *args, **kwargs):
    #     if self.default_rate:
    #         self.amount_paid = self.units * self.product.rate
    #     super(Sale, self).save(*args, **kwargs)

    # def save_amounts(self, units, rate, status):
    #     if status == 'fully paid':
    #         self.amount_paid = units * rate
    #     elif status == 'partly paid':
    #         self.amount_balance = (units * rate) - self.amount_paid
    #     else:
    #         self.amount_balance = units * rate
    #     return self.amount_paid



