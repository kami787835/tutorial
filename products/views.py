from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Lesson, UserProfile,Group
from .serializers import LessonSerializer, UserProfileSerializer, GroupSerializer, \
    ProductWithLessonCountSerializer
from rest_framework.decorators import action

class ProductViewSet(viewsets.ModelViewSet):
    # ... ваш существующий код ...

    @action(detail=False, methods=['get'])
    def available_products(self, request):
        # Получаем профиль пользователя
        user_profile = UserProfile.objects.get(user=request.user)

        # Получаем доступные для пользователя продукты
        user_products = user_profile.available_products.all()

        # Сериализуем данные о доступных продуктах
        serializer = ProductWithLessonCountSerializer(user_products, many=True)
        return Response(serializer.data)

def available_products_view(request):
    user_profile = request.user.userprofile
    user_products = user_profile.available_products.all()
    serialized_products = ProductWithLessonCountSerializer(user_products, many=True).data
    return render(request, 'products.html', {'available_products': serialized_products})

class LessonViewSet(viewsets.ModelViewSet):
    # ... ваш существующий код ...

    @action(detail=False, methods=['get'])
    def lessons_by_product(self, request):
        # Получаем профиль пользователя
        user_profile = UserProfile.objects.get(user=request.user)

        # Получаем доступные для пользователя продукты
        user_products = user_profile.available_products.all()

        # Получаем уроки для всех доступных продуктов
        lessons = Lesson.objects.filter(product__in=user_products)

        # Сериализуем данные о уроках
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer