from django.contrib import admin
from .models import Product, Lesson, UserProfile, Group

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'start_date_time', 'cost')
    search_fields = ('name', 'creator__username')
    change_form_template = 'admin/change_form.html'

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'video_link')
    search_fields = ('name', 'product__name')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user__username', )

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'min_users', 'max_users')
    search_fields = ('name', 'product__name')
