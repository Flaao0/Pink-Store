from django.shortcuts import render
from .models import Review

# Create your views here.

def review_list(request):
    review_db = Review.objects.all()
    context = {
        "reviews": review_db
    }
    return render(request, 'review/review_list.html', context)