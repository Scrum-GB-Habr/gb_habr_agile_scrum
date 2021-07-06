from django.contrib import admin
from .models import Post, Contact, Category, SubCategory, ArticleSubcat
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at']

@admin.register(Contact)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'message_description', 'email']

@admin.register(Category)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat_name', 'description', 'date_obsolete', 'date_create',
                    'date_update', 'comment']

@admin.register(SubCategory)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'subcat_name', 'description', 'date_obsolete',
                    'date_create', 'date_update', 'comment']

@admin.register(ArticleSubcat)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'subcat', 'date_create']

