from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=5)
    
    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        
    def __str__(self):
        return f"{self.product} {self.text} ({self.rating})"