from django.shortcuts import render
from django.views.generic import ListView

from .models import Customer


class CustomerList(ListView):
    template_name = 'customers/home.html'
    context_object_name = 'customer_list'
    queryset = Customer.objects.filter(active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(CustomerList, self).get_context_data(*args, **kwargs)
        context['no_inactive'] = Customer.objects.filter(active=False).count()

        return context
