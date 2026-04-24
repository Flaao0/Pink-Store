from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    profile_mock = User.objects.first()
    context = {
        "user": profile_mock,
    }
    return render(request, 'users/profile.html', context)