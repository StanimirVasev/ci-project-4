from django import forms
from django.forms import ModelForm, ModelChoiceField
from .models import ProductReview, Product

class ProductReviewForm(forms.ModelForm):
    reviewed_product = ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = ProductReview
        fields = ('review_title', 'reviewed_product', 'reviewer', 'review', 'date')
        widgets = {'reviewer': HiddenInput(), 'date': HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_placeholders = {
            'review_title': 'Review Title',
            'reviewed_product': 'Reviewed Product',
            'reviewer': 'Reviewed By',
            'review': 'Your Review',
            'date': 'Date & Time',
        }

        self.fields['review_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{field_placeholders[field]} *'
            else:
                placeholder = field_placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

    def clean(self):
        cleaned_data = super().clean()
        review_title = cleaned_data.get('review_title')
        review = cleaned_data.get('review')
        if not review_title or not review:
            raise forms.ValidationError('Please enter a review title and review text')
        return cleaned_data