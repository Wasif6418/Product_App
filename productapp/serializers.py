from rest_framework import serializers, generics

from .models import SubCategory,Category, Brand, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'color', 'created_date', 'created_by', 'updated_date', 'updated_by', 'description', 'price', 'subcategory_id')
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'slug',  'created_date', 'created_by', 'updated_date', 'updated_by', 'description',  'category_id')
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug',  'created_date', 'created_by', 'updated_date', 'updated_by',  'brand_id')
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'slug',  'created_date', 'created_by', 'updated_date', 'updated_by',)
