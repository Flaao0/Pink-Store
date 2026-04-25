from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Оставили только телефон
        fields = ['phone'] 

        labels = {
            'phone': 'Номер телефона',
        }
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+7 (999) 000-00-00'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        
        if not phone:
            return phone
            
        clean_p = phone.replace(' ', '').replace('-', '')
        
        if not clean_p.replace('+', '').isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры!")
            
        if not (clean_p.startswith('+7') or clean_p.startswith('8')):
            raise forms.ValidationError("Номер должен начинаться с +7 или 8!")
            
        return phone