from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from apps.products.models import Product
from django.http import JsonResponse
from .serializer import CartItemSerializer
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET"])
def get_cart_items(request):
    pass


api_view(["POST"])


def remove_cart_item(request):
    if request.POST:
        CartItem.objects.get(pk=request.data["cart_item_pk"]).delete()
        cart = get_object_or_404(Cart, pk=request.session["cart_id"])
        return JsonResponse(
            {
                "response": "item deleted",
                "total_price": cart.get_total_cost(),
                "total_items": cart.cart_item.count(),
            }
        )

    else:
        return JsonResponse({"response": "fail to delete the item"})


@api_view(["POST"])
def add_cart_item(request):
    if request.POST:
        product = get_object_or_404(
            Product, pk=request.data["product_pk"], available=True
        )
        quantity = int(request.data["quantity"])
        if quantity >= 1 and quantity <= 10:
            if "cart_id" in request.session:
                cart = get_object_or_404(Cart, pk=request.session["cart_id"])
            else:
                cart = Cart.objects.create()
                request.session["cart_id"] = cart.id

            cart_item_update, cart_item_created = CartItem.objects.get_or_create(
                product=product,
                price=product.real_price,
                cart=cart,
            )
            if cart_item_created:
                cart_item_update.quantity = quantity
            else:
                cart_item_update.quantity = cart_item_update.quantity + quantity
            cart_item_update.save()

        return JsonResponse({"response": "Cart Updated"})
    else:
        return JsonResponse({"response": "Fail To Insert Item"})
