# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

# Create your models here.
