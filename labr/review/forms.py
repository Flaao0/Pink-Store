from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['text', 'rating'] # тут мы указываем только те поля,которые должен заполнять сам пользователь