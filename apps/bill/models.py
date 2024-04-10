from django.db import models

# from accounts.models import User


class Bill(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return "Order {}".format(self.id)

    def get_total_cost(self):
        return sum(item.get_total_cost() for item in self.cart_bill.all())

    def get_products_name(self):
        products_name = ""
        for item in self.cart_bill.all():
            if products_name:
                products_name = f"{item.product.product_name},"
            else:
                products_name = f"{products_name},{item.product.product_name}"
        return products_name

    def get_order_id(self):
        return f"{self.pk}"
