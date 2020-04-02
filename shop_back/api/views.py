from django.http.response import JsonResponse
from django.http import Http404

from api.models import Product, Category


def to_json(items):
    return [item.to_json() for item in items]


def products(request):
    return JsonResponse(to_json(Product.objects.all()), safe=False)


def get_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    return JsonResponse(product.to_json())


def categories(request):
    return JsonResponse(to_json(Category.objects.all()), safe=False)


def get_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404
    return JsonResponse(category.to_json())


def get_category_products(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404

    return JsonResponse(to_json(Product.objects.filter(category_id=id)), safe=False)
