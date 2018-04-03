from django import forms

from .models import Sale, Product


class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()
        self.fields['status'].initial = Sale.STATUS_CHOICES[0][0]
        # self.fields['amount_paid'].disabled = True

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
                'class': 'form-control',
            }),
            'amount_paid': forms.NumberInput(attrs={
                'class': 'form-control',
            }),

        }



