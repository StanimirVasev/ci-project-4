from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Post(models.Model):
    title = models.CharField(max_length=255)
    friendly_title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title

    def get_friendly_title(self):
        return self.friendly_title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    friendly_author = models.CharField(max_length=60, null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

    def get_friendly_author(self):
        return self.friendly_author