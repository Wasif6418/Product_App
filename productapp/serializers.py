from rest_framework import serializers, generics

from .models import SubCategory,Category, Brand, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'color','suggestions' ,'created_date', 'created_by', 'updated_date', 'updated_by', 'description', 'price', 'subcategory_id')
class SubcategorySerializer(serializers.ModelSerializer):
    products= ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'slug',  'created_date', 'created_by', 'updated_date', 'updated_by', 'description',  'category_id', 'products')
class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug',  'created_date', 'created_by', 'updated_date', 'updated_by',  'brand_id', 'subcategories')
class BrandSerializer(serializers.ModelSerializer):
    categories= CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ('id', 'name', 'slug',  'created_date', 'created_by', 'updated_date', 'updated_by','categories')
