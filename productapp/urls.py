from django.urls import path

from productapp import views
from .views import ProductDetailView, SubCategoryDetailView, CategoryDetailView, BrandDetailView



urlpatterns = [
    path('products/<slug:slug>/',  ProductDetailView.as_view()),
    path('subcategory/<slug:slug>/', SubCategoryDetailView.as_view()),
    path('category/<slug:slug>/', CategoryDetailView.as_view()),
    path('brand/<slug:slug>/', BrandDetailView.as_view())
]