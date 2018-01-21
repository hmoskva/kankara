from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='Customer Name')
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
