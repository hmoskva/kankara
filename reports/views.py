from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from sales.models import Sale
from .filters import SaleFilter


# def home(request):
#     return render(request, 'reports/home.html')

@login_required
def search(request):
    data = dict()
    sale_list = Sale.objects.all()
    sale_filter = SaleFilter(request.GET, queryset=sale_list)

    print(sale_filter.qs)

    data['html_report_list'] = render_to_string('sales/includes/sales_table.html', {
        'sales_list': sale_filter.qs}, request=request)
    if request.is_ajax():
        return JsonResponse(data)
    return render(request, 'reports/home.html', {'filter': sale_filter})
