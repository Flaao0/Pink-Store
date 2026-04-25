from django.shortcuts import render, redirect
from .models import Product, Category
from django.shortcuts import render, get_object_or_404
from review.models import Review
from review.forms import ReviewForm
from django.contrib.auth.models import User
from django.urls import reverse

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
    form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }
    
    return render(request, 'catalog/product_detail.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    product_id_str = str(product.id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart
    return redirect('catalog:cart_view')


def cart_view(request):
    cart = request.session.get('cart', {})
    product_ids = [int(product_id) for product_id in cart.keys()]
    products = Product.objects.filter(id__in=product_ids)

    items = []
    total_price = 0

    for product in products:
        qty = cart.get(str(product.id), 0)
        line_total = product.price * qty
        total_price += line_total
        items.append({
            'product': product,
            'qty': qty,
            'line_total': line_total,
        })

    context = {
        'items': items,
        'total_price': total_price,
    }
    return render(request, 'catalog/cart.html', context)


def clear_cart(request):
    request.session['cart'] = {}
    return redirect('catalog:cart_view')


def toggle_theme(request):
    current_theme = request.COOKIES.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    next_url = request.META.get('HTTP_REFERER') or reverse('catalog:home')
    response = redirect(next_url)
    response.set_cookie('theme', new_theme, max_age=60 * 60 * 24 * 365, path='/')
    return response
