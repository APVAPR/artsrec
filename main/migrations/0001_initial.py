# Generated by Django 3.2.9 on 2021-11-19 17:04

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
                ('title', models.CharField(max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория')),
                ('title_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item', verbose_name='Название')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Фото')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item', verbose_name='Название')),
            ],
        ),
    ]