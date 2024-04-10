from django.db import models
from apps.products.models import Product
from apps.bill.models import Bill

# from accounts.models import User


class Cart(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return "cart {}".format(self.id)

    def get_total_cost(self):
        return sum(item.get_total_cost() for item in self.cart_item.all())


class CartItem(models.Model):
    bill = models.ForeignKey(
        Bill,
        related_name="cart_bill",
        null=True,
        on_delete=models.CASCADE,
    )
    cart = models.ForeignKey(
        Cart,
        related_name="cart_item",
        null=True,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name="cart_product",
        on_delete=models.CASCADE,
    )

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.product.product_name)

    def get_total_cost(self):
        return self.price * self.quantity
