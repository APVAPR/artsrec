from django.shortcuts import render

from .models import *

menu = ['На главную', 'Книги', 'Фильмы', 'Игры', 'Рекомендовать']

all_posts = Post.objects.all()
last_post = Post.objects.last()
images = Image.objects.all()
last_post_image = Image.objects.last().photo


def index(requests):

    return render(requests, 'main/index.html', {'title': 'Recommendation',
                                                'nav_buttons': menu,
                                                'posts': all_posts,
                                                'last_post': last_post,
                                                'last_post_photo': last_post_image,
                                                'image': images})


def post(requests, username, post):

    return render(requests, 'main/post.html', last_post)


def categories(requests):
    return render(requests, 'main/categories.html')
