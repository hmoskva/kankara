from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from businesses.models import Business
from customers.models import Customer
from products.models import Product


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        context['business_list'] = Business.objects.filter(active=True)
        context['customers'] = Customer.objects.filter(active=True).count()
        context['products'] = Product.objects.all().count()
        return context