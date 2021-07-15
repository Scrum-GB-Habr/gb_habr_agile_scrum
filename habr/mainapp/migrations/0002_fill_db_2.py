import os

from django.conf import settings
from django.db import migrations


def forwards_func(apps, schema_editor):
    if settings.DEBUG:
        os.system('python manage.py loaddata mainapp')


def reverse_func(apps, schema_editor):
    if settings.DEBUG:
        myModels = [apps.get_model("authapp", "mainapp"),
        ]
        for myModel in myModels:
           myModel.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [migrations.RunPython(forwards_func, reverse_func)]