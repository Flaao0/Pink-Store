from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        
    def __str__(self):
        return f"{self.user.username}({self.phone})"