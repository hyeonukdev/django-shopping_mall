from django.urls import path
from . import views

app_name = "category_page"

urlpatterns = [
    path('', views.category_page, name='categories'),
]