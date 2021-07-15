from django.contrib import admin
from .models import AuthorizedUser

@admin.register(AuthorizedUser)
class PostModelAdmin(admin.ModelAdmin):
    pass