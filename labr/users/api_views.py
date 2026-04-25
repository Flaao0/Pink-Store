from rest_framework import generics, permissions
from users.models import Profile
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(
    summary="Профиль текущего пользователя",
    description="Возвращает профиль авторизованного пользователя",
    tags=['Пользователи']
) 
class MyProfileAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)