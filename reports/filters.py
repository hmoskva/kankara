from django.conf import settings

from sales.models import Sale
import django_filters


class SaleFilter(django_filters.FilterSet):

    class Meta:
        model = Sale
        fields = ['business', 'customer', 'product', 'status', 'created_by',
                  'date_created']





