from django.db import models
from django.contrib.auth.models import AbstractUser


class AuthorizedUser(AbstractUser):
    pass
    # Сделал чтобы просто создать модельку, а что сюда добавить не придумал