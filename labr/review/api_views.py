from rest_framework import generics
from review.models import Review
from .serializers import ReviewSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    summary="Список отзывов",
    description="Возвращает список всех отзывов ко всем товарам",
    tags=['Отзывы']
) 
class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
@extend_schema(
    summary="Детальная информация об отзыве",
    description="Возвращает один отзыв по его id",
    tags=['Отзывы']
) 
class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer