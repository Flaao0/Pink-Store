from django.shortcuts import render
from .models import Product, Category

# Create your views here.
MOCK_PRODUCTS = [
    {'name': 'Худи оверсайз', 'price': 3500, 'in_stock': True},
    {'name': 'Кроссовки', 'price': 5200, 'in_stock': True},
    {'name': 'Рюкзак городской', 'price': 2100, 'in_stock': False},
]

def home_page(request):
    return render(request, 'catalog/home.html')

def product_list(request):
    products_db = Product.objects.all()
    categories_db = Category.objects.all()
    context = {
        "products": products_db,
        "categories": categories_db,
        }
    return render(request, 'catalog/product_list.html', context)