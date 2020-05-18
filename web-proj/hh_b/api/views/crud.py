import json

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from api.models import Company, Vacancy, Category, Product


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [c.to_json() for c in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        companies = Company.objects.create(name=data.get('name'))
        return JsonResponse(companies.to_json())


#     company_list-->category_list
@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        categories_json = [c.to_json() for c in categories]
        return JsonResponse(categories_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        categories = Category.objects.create(name=data.get('name'))
        return JsonResponse(categories.to_json())


@csrf_exempt
class CompanyList(View):
    def get(self, request):
        companies = Company.objects.all()
        companies_json = [c.to_json() for c in companies]
        return JsonResponse(companies_json, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        companies = Company.objects.create(name=data.get('name'))
        return JsonResponse(companies.to_json)


#           CompanyList-->CategoryList
@csrf_exempt
class CategoryList(View):
    def get(self, request):
        categories = CategoryList.objects.all()
        categories_json = [c.to_json() for c in categories]
        return JsonResponse(categories_json, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        categories = Category.objects.create(name=data.get('name'))
        return JsonResponse(categories.to_json)


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data.get('name', company.name)
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
class CompanyDetails(View):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        JsonResponse(company.to_json())

    def put(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
            data = json.loads(request.body)
            company.name = data.get('name', company.name)
            company.save()
            return JsonResponse(company.to_json())
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def delete(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
            company.delete()
            return JsonResponse({'deleted': True})
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})


#         CompanyDetails-->CategoryDetails
@csrf_exempt
def category_detail(request, category_id):
    try:
        categories = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(categories.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        categories.name = data.get('name', categories.name)
        categories.save()
        return JsonResponse(categories.to_json())
    elif request.method == 'DELETE':
        categories.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
class CategoryDetails(View):
    def get(self, request, category_id):
        try:
            categories = Category.objects.get(id=category_id)
        except Category.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        JsonResponse(categories.to_json())

    def put(self, request, category_id):
        try:
            categories = Category.objects.get(id=category_id)
            data = json.loads(request.body)
            categories.name = data.get('name', categories.name)
            categories.save()
            return JsonResponse(categories.to_json())
        except Category.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def delete(self, request, category_id):
        try:
            categories = Company.objects.get(id=category_id)
            categories.delete()
            return JsonResponse({'deleted': True})
        except Category.DoesNotExist as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def company_vacancies(request, company_id):
    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company_id=company_id)
        vacancies_json = [c.to_json() for c in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        vacancies = Vacancy.objects.create(name=data.get('name'))
        return JsonResponse(vacancies.to_json())


@csrf_exempt
class CompanyVacancies(View):
    def get(self, request, company_id):
        vacancies = Vacancy.objects.filter(company_id=company_id)
        vacancies_json = [c.to_json() for c in vacancies]
        return JsonResponse(vacancies_json, safe=False)

    def post(self, request, company_id):
        data = json.loads(request.body)
        vacancies = Vacancy.objects.create(name=data.get('name'))
        return JsonResponse(vacancies.to_json())


#     CompanyVacancies-->CategoryProducts
@csrf_exempt
def category_products(request, category_id):
    if request.method == 'GET':
        products = Product.objects.filter(category_id=category_id)
        products_json = [c.to_json() for c in products]
        return JsonResponse(products_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        products = Product.objects.create(name=data.get('name'))
        return JsonResponse(products.to_json())


@csrf_exempt
class CategoryProducts(View):
    def get(self, request, category_id):
        products = Product.objects.filter(category_id=category_id)
        products_json = [c.to_json() for c in products]
        return JsonResponse(products_json, safe=False)

    def post(self, request, category_id):
        data = json.loads(request.body)
        categories = Category.objects.create(name=data.get('name'))
        return JsonResponse(categories.to_json())


@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [c.to_json() for c in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        vacancies = Vacancy.objects.create(name=data.get('name'))
        return JsonResponse(vacancies.to_json())


@csrf_exempt
class VacancyList(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        vacancies_json = [c.to_json() for c in vacancies]
        return JsonResponse(vacancies_json, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        vacancies = Vacancy.objects.create(name=data.get('name'))
        return JsonResponse(vacancies.to_json())

    #     VacancyList-->ProductList
    @csrf_exempt
    def product_list(request):
        if request.method == 'GET':
            products = Product.objects.all()
            products_json = [c.to_json() for c in products]
            return JsonResponse(products_json, safe=False)
        elif request.method == 'POST':
            data = json.loads(request.body)
            products = Product.objects.create(name=data.get('name'))
            return JsonResponse(products.to_json())

    @csrf_exempt
    class ProductList(View):
        def get(self, request):
            products = Product.objects.all()
            products_json = [c.to_json() for c in products]
            return JsonResponse(products_json, safe=False)

        def post(self, request):
            data = json.loads(request.body)
            products = Product.objects.create(name=data.get('name'))
            return JsonResponse(products.to_json())


@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        vacancy.name = data.get('name', vacancy.name)
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
class VacancyDetails(View):
    def get(self, request, vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            return JsonResponse(vacancy.to_json())
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def put(self, request, vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            data = json.loads(request.body)
            vacancy.name = data.get('name', vacancy.name)
            vacancy.save()
            return JsonResponse(vacancy.to_json())
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def delete(self, request, vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            vacancy.delete()
            return JsonResponse({'deleted': True})
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
#       VacancyDetail-->ProductDetail
@csrf_exempt
def products_detail(request, product_id):
    try:
        products = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(products.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        products.name = data.get('name', products.name)
        products.save()
        return JsonResponse(products.to_json())
    elif request.method == 'DELETE':
        products.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
class ProductDetails(View):
    def get(self, request, product_id):
        try:
            products = Product.objects.get(id=product_id)
            return JsonResponse(products.to_json())
        except Product.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def put(self, request, product_id):
        try:
            products = Product.objects.get(id=product_id)
            data = json.loads(request.body)
            products.name = data.get('name', products.name)
            products.save()
            return JsonResponse(products.to_json())
        except Product.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def delete(self, request, product_id):
        try:
            products = Vacancy.objects.get(id=product_id)
            products.delete()
            return JsonResponse({'deleted': True})
        except Product.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
