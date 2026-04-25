from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        
    def __str__(self):
        status = "Оплачен" if self.is_paid else "Не оплачен"
        return f"Заказ №{self.id} от {self.user.username} ({status})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='Товар')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField(default=1)
    
    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"
        
    def __str__(self):
        return f"{self.product.title} ({self.quantity} шт.) в Заказе №{self.order.id}"