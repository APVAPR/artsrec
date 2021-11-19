from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    title_post = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title_post


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.title} {self.author}'


class Image(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name="Название")
    photo = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name='Фото')


