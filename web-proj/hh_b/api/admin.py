from django.contrib import admin
from api.models import Company, Vacancy, Category


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'city', 'address')


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'salary', 'company_id')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
