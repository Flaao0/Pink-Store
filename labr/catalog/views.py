from django.shortcuts import redirect, render
from .models import Product, Category
from django.shortcuts import render, get_object_or_404
from review.models import Review
from review.forms import ReviewForm
from django.contrib.auth.models import User

# Create your views here.

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


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        # Заполняем форму присланными данными
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            # Создаем объект отзыва, но пока не сохраняем в БД
            new_review = form.save(commit=False)
            
            # Привязываем товар и временного автора (костыль до внедрения Auth)
            new_review.product = product
            new_review.user = User.objects.first()
            
            # Сохраняем в базу данных
            new_review.save()
            
            # Редирект для предотвращения повторной отправки формы (PRG pattern)
            return redirect('catalog:product_detail', product_id=product.id)
    else:
        # Если GET-запрос — создаем пустую форму
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }
    
    return render(request, 'catalog/product_detail.html', context)
