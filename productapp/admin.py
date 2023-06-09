from django.contrib import admin
from .models import *
from admin_searchable_dropdown.filters import AutocompleteFilter



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'slug', 'created_date', 'created_by', 'updated_date', 'updated_by')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name','slug']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'slug', 'created_date', 'created_by', 'updated_date', 'updated_by', 'brand_id')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug', 'brand_id']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'created_date', 'created_by', 'updated_date', 'updated_by', 'category_id')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name','slug','description','category_id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'slug', 'color', 'description', 'price', 'created_date', 'created_by', 'updated_date', 'updated_by', 'subcategory_id')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name','slug', 'color','description', 'price', 'subcategory_id']



class CarCompanyFilter(AutocompleteFilter):
    title = 'Company' # display title
    field_name = 'company' # name of the foreign key field


class CarCompanyAdmin(admin.ModelAdmin):
    search_fields = ['name'] # this is required for django's autocomplete functionality
    # ...


class CarModelAdmin(admin.ModelAdmin):
    list_filter = [CarCompanyFilter]


