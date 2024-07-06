from django import forms
from .models import Product, Category, Subcategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.name, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        subcategories = Subcategory.objects.all()
        subcategory_friendly_names = [(subcat.name, subcat.get_friendly_name()) for subcat in subcategories]
        self.fields['subcategory'].choices = subcategory_friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'