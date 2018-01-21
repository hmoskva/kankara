from django import forms

from .models import Sale


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        exclude = ['date_modified', 'date_created', 'created_by', 'timestamp']
        widgets = {
            'business': forms.Select(attrs={
                'class': 'form-control'
            }),
            'customer': forms.Select(attrs={
                'class': 'form-control'
            }),
            'product': forms.Select(attrs={
                'class': 'form-control'

            }),
            'units': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'default_rate': forms.CheckboxInput(attrs={
                'class': 'form-control'
            }),
            'amount_paid': forms.NumberInput(attrs={
                'class': 'form-control',
            }),

        }



