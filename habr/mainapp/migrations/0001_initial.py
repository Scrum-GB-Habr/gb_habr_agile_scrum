# Generated by Django 3.2.4 on 2021-07-30 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='активна')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создана')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='изменена')),
                ('comment', models.CharField(blank=True, max_length=1000, verbose_name='комментарий администратора')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message_description', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='активна')),
                ('on_moderation', models.BooleanField(default=False, verbose_name='на модерации')),
                ('published', models.BooleanField(default=False, verbose_name='опубликована')),
                ('rejected', models.BooleanField(default=False, verbose_name='отменена')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='mainapp.Category', verbose_name='категории статей')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
