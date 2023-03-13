from django.urls import path
from .views import ProductList, SubCategorylist, Category, BrandList
from productapp import views

urlpatterns = [
    path('products/<slug:slug>', views.ProductList.as_view()),
    path('subcategory/<slug:slug>', views.SubCategorylist.as_view()),
    path('category/<slug:slug>', views.Category.as_view()),
    path('brand/', views.BrandList.as_view(), name='BrandList')
]