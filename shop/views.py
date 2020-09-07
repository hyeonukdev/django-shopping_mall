from django.shortcuts import render, get_object_or_404

from .models import *

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "shop/list_t_mshirts.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
        "shop/list_t_wshirts.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
        "long_shirts/list_l_mshirts.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
        "long_shirts/list_l_wshirts.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
        "onepeace/list_onepeace.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
        "shorts_pants/list_s_wpants.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
        "shorts_pants/list_s_mpants.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
        "coats/list_mcoats.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
        "coats/list_wcoats.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
        "long_pants/list_l_mpants.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
        "long_pants/list_l_wpants.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )

#short shirts
def wshort_shirts_product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.filter(name='여성반팔티')
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "shop/list_t_wshirts.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )
def mshort_shirts_product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.filter(name='남성반팔티')
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "shop/list_t_mshirts.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )

#long shirts
def mlong_shirts_product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.filter(name='남성긴팔티')
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "long_shirts/list_l_mshirts.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )

def wlong_shirts_product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.filter(name='여성긴팔티')
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "long_shirts/list_l_wshirts.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )

#onepeace
def onepeace_product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.filter(name='여성원피스')
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "onepeace/list_onepeace.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )

#short pants
def mshort_pants_product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.filter(name='남성반바지')
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "short_pants/list_s_mpants.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )
def wshort_pants_product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.filter(name='여성반바지')
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "short_pants/list_s_wpants.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )

#long_pants
def mlong_pants_product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.filter(name='남성긴바지')
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "long_pants/list_l_mpants.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )

def wlong_pants_product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.filter(name='여성긴바지')
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "long_pants/list_l_wpants.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )


#coat
def mcoats_product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.filter(name='남성코트')
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "coats/list_mcoats.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )

def wcoats_product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.filter(name='여성코트')
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request,
        "coats/list_wcoats.html",
        {
            "current_category": current_category,
            "categories": categories,
            "products": products,
        },
    )

from cart.forms import AddProductForm

@method_decorator(csrf_exempt)
def product_detail(request, id, product_slug=None):

    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={"제품수량": 1})
    return render(
        request, "shop/detail.html", {"product": product, "add_to_cart": add_to_cart,},
    )


def get_category(request):
    categories = Category.objects.all()

    return render(request, "shop/detail.html", {},)
