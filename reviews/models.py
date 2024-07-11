from django.db import models
from profiles.models import UserProfile
from products.models import Product


class ProductReview(models.Model):
    review_title = models.CharField(
        max_length=90,
        null=False,
        blank=False
    )
    reviewed_product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    reviewer = models.ForeignKey(
        UserProfile,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    review = models.TextField(
        max_length=500
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.review_title
