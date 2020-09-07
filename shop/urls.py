from django.urls import path
from .views import *

app_name = "shop"

urlpatterns = [
    path("", product_in_category, name="product_all"),
    path("man_short_shirts", mshort_shirts_product_in_category, name="product_short_mshirts"),
    path("woman_short_shirts", wshort_shirts_product_in_category, name="product_short_wshirts"),
   
    path("mlong_shirts", mlong_shirts_product_in_category, name="product_long_mshirts"),
    path("wlong_shirts", wlong_shirts_product_in_category, name="product_long_wshirts"),

    path("man_short_pants", mshort_pants_product_in_category, name="product_short_mpants"),
    path("woman_short_pants", wshort_pants_product_in_category, name="product_short_wpants"),
    
    path("man_long_pants",mlong_pants_product_in_category, name="product_long_mpants"),
    path("woman_long_pants",wlong_pants_product_in_category, name="product_long_wpants"),
    
    path("man_coats", mcoats_product_in_category, name="product_mcoats"),
    path("woman_coats", wcoats_product_in_category, name="product_wcoats"),
    
    path("onepeace", onepeace_product_in_category, name="product_onepeace"),

    path("<slug:category_slug>/", product_in_category, name="product_in_category"),
    path("<int:id>/<product_slug>/", product_detail, name="product_detail"),
]