from django.shortcuts import render
from .models import Order
from django.contrib.auth.models import User

# Create your views here.

def order_list(request):
    order_db = Order.objects.all()
    user_mock = User.objects.first()
    context = {
        "orders": order_db,
        "user": user_mock,
    }
    return render(request, 'orders/order_list.html', context)