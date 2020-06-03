from django.shortcuts import render, get_object_or_404
# from ..shop.models import *
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# sys.path.append('../shop/')
# import models
from shop import models

def index(request, category_slug=None):
    current_category = None
    categories = models.Category.objects.all()
    products = models.Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(models.Category, slug=category_slug)
        products = products.filter(category=current_category)

    # return render(request, 'index.html')
    return render(
        request,
        "index.html",
        {
            "products": products,
        },       
    )
    