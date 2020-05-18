from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=300, default='name')
    description = models.TextField(default='')
    city = models.CharField(max_length=300, default='city')
    address = models.CharField(max_length=300, default='address')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=300, default='name')
    description = models.TextField(default='')
    salary = models.FloatField(default=1000)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company_id
        }


class Category(models.Model):
    name = models.CharField(max_length=300, default='name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name

        }


class Product(models.Model):
    name = models.CharField(max_length=300, default='name')
    imageLink1 = models.TextField(default='')
    imageLink2 = models.TextField(default='')
    description = models.TextField(default='')
    price = models.FloatField(default=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'imageLink1': self.imageLink1,
            'imageLink2': self.imageLink2,
            'description': self.description,
            'salary': self.price,
            'category': self.category_id
        }


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }


class Manager(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }


class Card(models.Model):
    products = models.ManyToManyField(Product)


from django.db import models

# Create your models here.
