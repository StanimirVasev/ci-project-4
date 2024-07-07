from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from profiles.models import UserProfile
from products.models import Product

# Model that allows users to review a product

class ProductReview(models.Model):

    review_title = models.CharField(max_length=90, null=False, blank=False)
    reviewed_product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE)
    review = models.TextField(
        max_length=500,
        validators=[MinLengthValidator(10), MaxLengthValidator(500)],
        help_text='Please enter a review between 10 and 500 characters'
    )
    date = models.DateTimeField(auto_now_add=True)

    # Corrects the spelling in Django admin

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.review_title

