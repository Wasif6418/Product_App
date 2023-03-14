from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL, related_name="brand_user_createdid")
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = UserForeignKey(auto_user=True, on_delete=models.SET_NULL, related_name="brand_user_updateid")

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL, related_name="categories_createdid")
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = UserForeignKey(auto_user=True, on_delete=models.SET_NULL, related_name='categories_updatedid')
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

# Create your models here.
class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL, related_name='subcategories_createdid')
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = UserForeignKey(auto_user=True, on_delete=models.SET_NULL, related_name='subcategories_updatedid')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    color = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL, related_name='products_createdid')
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = UserForeignKey(auto_user=True, on_delete=models.SET_NULL, related_name='products_updatedid')
    subcategory_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


