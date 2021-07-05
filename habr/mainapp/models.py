from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    title = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    message_description = models.TextField(max_length=50)


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    # Служебные
    date_obsolete = models.DateTimeField(null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.cat_name}{"(блок)" if self.date_obsolete else ""}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcat_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    # Служебные
    date_obsolete = models.DateTimeField(null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.subcat_name}{"(блок)" if self.date_obsolete else ""}'

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'


