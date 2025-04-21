from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель продукта')
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    start_date_time = models.DateTimeField(verbose_name='Дата и время начала')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость продукта')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукты'
        verbose_name_plural = 'продук'

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    name = models.CharField(max_length=255, verbose_name='Название урока')
    video_link = models.URLField(verbose_name='Ссылка на видео')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'урок'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    available_products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профиль'

class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    name = models.CharField(max_length=255, verbose_name='Название группы')
    min_users = models.PositiveIntegerField(verbose_name='Минимальное количество участников')
    max_users = models.PositiveIntegerField(verbose_name='Максимальное количество участников')
    members = models.ManyToManyField(User, related_name='product_groups', verbose_name='Ученики, состоящие в группе')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'группы'
        verbose_name_plural = 'группы'
