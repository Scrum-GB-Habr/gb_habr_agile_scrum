from django.db import models
from django.contrib.auth.models import AbstractUser


class AuthorizedUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True,
        verbose_name='аватар')
    age = models.PositiveSmallIntegerField(verbose_name='возвраст', default=18)
    about_me = models.TextField(blank=True, verbose_name='о себе')
    gender = models.CharField(
        max_length=6,
        blank=True,
        choices=GENDER_CHOICES,
        verbose_name='пол')
