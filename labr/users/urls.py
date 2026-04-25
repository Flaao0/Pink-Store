from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import register



app_name = 'users'

urlpatterns = [
    path("", views.profile, name="profile"),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

