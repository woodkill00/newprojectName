from django import forms

from apps.productApp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'price',
            'has_colours',
            # 'available_colours',
            'has_sizes',
            # 'available_sizes',
        ]
