from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    description = models.TextField(max_length=500)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d/", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    remainder = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("view_product", kwargs={'product_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created"]


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse("category", kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

