from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView, View, DetailView
from django.http import JsonResponse
from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from businesses.models import Business
from .models import Sale
from products.models import Product
from .forms import SaleForm


@login_required
def list_sale(request, slug):
    business = get_object_or_404(Business, slug=slug)
    sale_list = Sale.objects.this_week(business)
    sales = get_paginated(request, sale_list)
    total_today = Sale.objects.total_today(business)
    total_this_week = Sale.objects.total_this_week(business)
    context = {
        'week_sales_list': sales,
        'day_sales_list': Sale.objects.this_day(business),
        'total_amount_today': 'N{amount}'.format(amount=total_today['amount_paid__sum'] or 0),
        'total_amount_this_week': 'N{amount}'.format(amount=total_this_week['amount_paid__sum'] or 0),
        'num_fully_paid_this_week': Sale.objects.get_number_of_paid_sales_by_week(business),
        'num_partly_paid_this_week': Sale.objects.get_number_of_part_paid_sales_by_week(business),
        'num_debt_this_week': Sale.objects.get_number_of_debt_sales_by_week(business),
    }
    if request.is_ajax():
        pass
    return render(request, 'sales/home.html', context)


@login_required
def create_sale(request):
    data = dict()
    form = SaleForm(data=request.POST or None)
    if request.method == 'POST':
        # id_product = int(request.POST.get('product'))
        # print(id_product)
        # form.fields['product'].choices = [(id_product, id_product)]
        print(form.data)
        if form.is_valid():
            new_sale = form.save(commit=False)
            new_sale.created_by = request.user
            new_sale.save()
            data['saved'] = True
        else:
            data['saved'] = False
            data['errors'] = form.errors
            print(form.errors)
            print(form.non_field_errors())

    data['sale_form'] = render_to_string('sales/includes/sale_form.html', {
        'form': form, 'action_url': '/sale/create/', 'modal_title': 'Add record'
    }, request=request)
    return JsonResponse(data)


def get_paginated(request, queryset):
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 10)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    return results


def edit_sale(request, pk):
    data = dict()
    record = get_object_or_404(Sale, pk=pk)
    form = SaleForm(data=request.POST or None, instance=record or None)
    if request.method == 'POST':
        if form.is_valid():
            the_sale = form.save(commit=False)
            the_sale.save()
            data['is_saved'] = True
            data['message'] = 'Record successfully edited!'
            qs = Sale.objects.this_week(business=the_sale.business.id)
            data['html_sale_list'] = render_to_string(
                'sales/includes/sales_table.html',
                {'sales_list': get_paginated(request, qs)}
            )
            data['html_sale_list_paginator'] = render_to_string(
                'sales/includes/sales_table_paginator.html',
                {'sales': get_paginated(request, qs)}
            )
        else:
            data['is_saved'] = False

    data['sale_form'] = render_to_string(
        'sales/includes/sale_form.html',
        {'form': form, 'action_url': '/sale/edit/{pk}/'.format(pk=pk), 'modal_title': 'Edit record'},
        request=request)

    return JsonResponse(data)


def delete_sale(request, pk):
    data = dict()
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        qs = Sale.objects.this_week(business=sale.business)
        sale.delete()
        data['is_saved'] = True
        data['message'] = 'Record successfully deleted'
        data['html_sale_list'] = render_to_string(
            'sales/includes/sales_table.html',
            {'sales_list': get_paginated(request, qs)}
        )
        data['html_sale_list_paginator'] = render_to_string(
            'sales/includes/sales_table_paginator.html',
            {'sales': get_paginated(request, qs)}
        )

    else:
        data['sale_form'] = render_to_string('sales/includes/del_sale_form.html',
                                                 {'sale': sale}, request=request)
    return JsonResponse(data)


def get_products_api_view(request, pk):
    business = get_object_or_404(Business, pk=pk)
    products = business.products.all()
    returned_data = [{
        'id': x.pk,
        'name': x.name,
        'rate': x.rate
    } for x in products]
    data = {'products': returned_data}
    return JsonResponse(data)


def get_product_fixed_price(request, pk):
    data = dict()
    product = get_object_or_404(Product, pk=pk)
    data['rate'] = product.rate
    return JsonResponse(data)