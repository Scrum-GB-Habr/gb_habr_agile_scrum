# Generated by Django 3.1.3 on 2021-07-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorizeduser',
            name='age',
            field=models.PositiveIntegerField(default=0, verbose_name='возраст'),
        ),
    ]