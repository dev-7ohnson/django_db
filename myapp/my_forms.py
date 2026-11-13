from django import forms

from myapp.models import Product


# creating a form using django
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'code','cost','price','for_sale', 'pic']
