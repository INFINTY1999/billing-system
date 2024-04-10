from django.db import models
from django.urls import reverse


class Product(models.Model):
    slug = models.SlugField(
        max_length=200, db_index=True
    )  # , unique=True, default="product slug"
    product_name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        index_together = (("slug"),)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("product_page", args=[self.slug])
