from django.contrib import admin
from .models import Post, Contact, Category, SubCategory, ArticleSubcat


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at']


@admin.register(Contact)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'message_description', 'email']


@admin.register(Category)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'is_active', 'created_at',
                    'updated_at', 'comment']


@admin.register(SubCategory)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'description', 'is_active',
                    'created_at', 'updated_at', 'comment']


@admin.register(ArticleSubcat)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'subcat', 'created_at']

