from django.db import models

class BlogCategory(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = "blog categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name or self.name

class Post(models.Model):
    title = models.CharField(max_length=254)
    friendly_title = models.CharField(max_length=254, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    blog_categories = models.ManyToManyField(BlogCategory, related_name="posts")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_friendly_title(self):
        return self.friendly_title
