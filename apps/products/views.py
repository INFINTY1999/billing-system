from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from apps.product_cart.models import Cart, CartItem


def index_page(request):
    product = Product.objects.filter(available=True)

    context = {"products": product}

    if request.POST:
        product = get_object_or_404(
            Product, pk=request.POST["product_pk"], available=True
        )
        quantity = int(request.POST["quantity"])
        if "cart_id" in request.session:
            cart = get_object_or_404(Cart, pk=request.session["cart_id"])
        else:
            cart = Cart.objects.create()
            request.session["cart_id"] = cart.id

        cart_item_update, cart_item_created = CartItem.objects.get_or_create(
            product=product,
            price=product.price,
            cart=cart,
        )

        if cart_item_created:
            cart_item_update.quantity = quantity
        else:
            cart_item_update.quantity = cart_item_update.quantity + quantity
        cart_item_update.save()
        return redirect("cart_page")

    return render(request, "index.html", context)


def cart_page(request):
    if "cart_id" in request.session:
        cart = get_object_or_404(Cart, pk=request.session["cart_id"])
    else:
        return redirect("index_page")
    if request.POST:
        cart_item = get_object_or_404(CartItem, pk=request.POST["cart_item_pk"])

    context = {"cart_items": cart.cart_item.all()}

    return render(request, "cart.html", context)
