from django.urls import path
from .views import *

app_name = "shop"

urlpatterns = [
    path("", product_in_category, name="product_all"),
    path("short_shirts", short_shirts_product_in_category, name="product_short_shirts"),
    path("short_pants", short_pants_product_in_category, name="product_short_pants"),
    path("long_shirts", long_shirts_product_in_category, name="product_long_shirts"),
    path("long_pants",long_pants_product_in_category, name="product_long_pants"),
    path("coats", coats_product_in_category, name="product_coats"),
    path("onepeace", onepeace_product_in_category, name="product_onepeace"),
    path("<slug:category_slug>/", product_in_category, name="product_in_category"),
    path("<int:id>/<product_slug>/", product_detail, name="product_detail"),
]