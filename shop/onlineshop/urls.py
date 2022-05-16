from django.urls import path

from .views import *

urlpatterns = [
    path("", MainPage.as_view(), name="home"),
    path("<category_slug>", ProductsByCategory.as_view(), name="category"),
    path("view/<slug:product_slug>", ViewProduct.as_view(), name="product")
]
