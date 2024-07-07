from django.contrib import admin
from .models import ProductReview


class ProductReviewAdmin(admin.ModelAdmin):

    list_display = (
      'review_title',
      'reviewed_product',
      'reviewer',
      'date',
    )

    # Items in product review will be ordered via date
    ordering = ('date',)


admin.site.register(ProductReview, ProductReviewAdmin)