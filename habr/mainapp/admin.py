from django.contrib import admin
from .models import Post, Contact
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at']

@admin.register(Contact)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'message_description', 'email']
