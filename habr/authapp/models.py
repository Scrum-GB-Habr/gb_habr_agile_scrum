import uuid

from django.db import models
from django.utils.translation import gettext_lazy as t
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from . import managers

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(t('Email'), max_length=255, unique=True)
    nickname = models.CharField(t('Nickname'), max_length=120, unique=True)
    first_name = models.CharField(t('Firt Name'), max_length=255)
    last_name = models.CharField(t('Last Name'), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = managers.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    class Meta:
        verbose_name = t('Пользователь')
        verbose_name_plural = t('Пользователи')
        db_table = 'user_accounts'
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return self.first_name
    
    def has_permissions(self, permission, obj=None):
        return True
    
    def has_module_permissions(self, app_label):
         return True
    
    @property
    def get_nickname(self):
        return self.nickname
    
    @property
    def is_staff(self):
         return self.is_admin
    
    def __str__(self):
         return self.email
    
    def save(self, *args, **kwargs):
        if not self.password:
            self.password = str(uuid.uuid4()).replace('-', '')
        super(User, self).save(*args, **kwargs)

