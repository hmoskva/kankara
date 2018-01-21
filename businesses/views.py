from django.shortcuts import render
from django.views.generic import ListView

from .models import Business


class BusinessList(ListView):
    queryset = Business.objects.filter(active=True)
    context_object_name = 'business_list'

    def get_context_data(self, *args, **kwargs):
        context = super(BusinessList, self).get_context_data(*args, **kwargs)
        return context




