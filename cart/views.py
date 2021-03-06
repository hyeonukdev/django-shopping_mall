from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .forms import AddProductForm
from .cart import Cart

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt)
@require_POST
def add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = AddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd["제품수량"], is_update=cd["is_update"])

    return redirect("cart:detail")


def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:detail")


def detail(request):
    cart = Cart(request)
    for product in cart:
        product["quantity_form"] = AddProductForm(
            initial={"제품수량": product["quantity"], "is_update": True}
        )
    return render(request, "cart/detail.html", {"cart": cart})
