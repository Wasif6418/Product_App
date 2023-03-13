
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Product, Category, Brand, SubCategory
from productapp.serializers import ProductSerializer,SubcategorySerializer,CategorySerializer,BrandSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']
class SubCategorylist(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']
class Category(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']
class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']


