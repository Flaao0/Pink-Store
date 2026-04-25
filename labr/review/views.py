from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Review
from .forms import ReviewForm
from catalog.models import Product

# Create your views here.

def review_list(request):
    review_db = Review.objects.all()
    context = {
        "reviews": review_db
    }
    return render(request, 'review/review_list.html', context)


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method != 'POST':
        return redirect('catalog:product_detail', product_id=product.id)

    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.product = product
        new_review.user = request.user
        new_review.save()

    return redirect('catalog:product_detail', product_id=product.id)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_detail', product_id=review.product.id)
    else:
        form = ReviewForm(instance=review)

    context = {
        "form": form,
        "review": review,
    }
    return render(request, "review/review_edit.html", context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        product_id = review.product.id
        review.delete()
        return redirect('catalog:product_detail', product_id=product_id)

    context = {
        "review": review,
    }
    return render(request, "review/review_confirm_delete.html", context)