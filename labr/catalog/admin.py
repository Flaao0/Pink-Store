from django.contrib import admin
from .models import Product, Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # слаг заполнится сам из названия
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Колонки, которые мы видим в общем списке
    list_display = ('title', 'category', 'price', 'stock', 'is_awaiable')
    # Поля, которые можно редактировать прямо в списке (Excel-style)
    list_editable = ('price', 'stock', 'is_awaiable')
    # Фильтры справа
    list_filter = ('is_awaiable', 'category')
    # Поиск по названию
    search_fields = ('title', 'description')