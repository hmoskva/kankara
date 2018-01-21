from django.db import models

from businesses.models import Business


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    business = models.ForeignKey(Business, related_name='products')
    rate = models.IntegerField()
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

