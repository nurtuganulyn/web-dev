from django.urls import path
from api.views import products, get_product, categories, get_category, get_category_products
urlpatterns = [
    path('products/', products),
    path('products/<int:id>/', get_product),
    path('categories/', categories),
    path('categories/<int:id>/', get_category),
    path('categories/<int:id>/products/', get_category_products),
]