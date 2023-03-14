from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Product, Category, Brand, SubCategory
from productapp.serializers import ProductSerializer,SubcategorySerializer,CategorySerializer,BrandSerializer


class ProductDetailView(APIView):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug.lower())  # filter by slug
        serializer = ProductSerializer(product)
        return Response(serializer.data)
class SubCategoryDetailView(APIView):
    def get(self, request, slug):
        subCategory = get_object_or_404(SubCategory, slug=slug.lower())  # filter by slug
        serializer = SubcategorySerializer(subCategory)
        return Response(serializer.data)
class CategoryDetailView(APIView):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug.lower())  # filter by slug
        serializer = CategorySerializer(category)
        return Response(serializer.data)
class BrandDetailView(APIView):
    def get(self, request, slug):

        brand = get_object_or_404(Brand, slug=slug.lower())  # filter by slug
        #brand = Brand.objects.filter(name__iexact=name).prefetch_related('categories__subcategories__products').first()

        serializer = BrandSerializer(brand)
        return Response(serializer.data)


