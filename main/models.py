from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    title_post = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name='Название', related_name='get_posts')
    content = models.TextField(blank=True, verbose_name="Текст статьи")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}: {self.title_post}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'user': self.user.username, 'slug': self.title_post.slug})

    class Meta:
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендации'
        ordering = ['date_create']


class Item(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 null=True, verbose_name="Категория",
                                 related_name='get_items')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.author}: {self.title}'

    class Meta:
        verbose_name = 'Название контента'
        verbose_name_plural = 'Названия контента'


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Рекомендация')
    photo = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name='Фото')

    def __str__(self):
        return f'Фото к посту {self.post}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['post']
