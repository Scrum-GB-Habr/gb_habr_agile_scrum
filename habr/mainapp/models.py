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
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=1000, blank=True, verbose_name='описание')
    # Служебные
    is_active = models.BooleanField(default=True, verbose_name='активна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='изменена')
    comment = models.CharField(max_length=1000, blank=True, verbose_name='комментарий администратора')

    def __str__(self):
        return f'{self.name}{"" if self.is_active else "(блок)"}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='родительская категория')
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=1000, blank=True, verbose_name='описание')
    # Служебные
    is_active = models.BooleanField(default=True, verbose_name='активна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='изменена')
    comment = models.CharField(max_length=1000, blank=True, verbose_name='комментарий администратора')

    def __str__(self):
        return f'{self.name}{"" if self.is_active else "(блок)"}'

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'


class ArticleSubcat(models.Model):
    article = models.ForeignKey(Post, on_delete=models.PROTECT, verbose_name='статья')
    subcat = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name='подкатегория')
    # Служебные
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.article}-{self.subcat}'

    class Meta:
        verbose_name = 'подкатегория статьи'
        verbose_name_plural = 'подкатегории статьи'
        # db_table = 'mainapp_articlesubcat'
        constraints = [
            models.UniqueConstraint(fields=['article', 'subcat'], name='unique_article_subcat')
        ]

