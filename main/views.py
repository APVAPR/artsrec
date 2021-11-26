from django.shortcuts import render

from .models import *

menu = [
    {'title': 'На главную', 'url':
        {'view': 'index', 'arg': None}},
    {'title': 'Книги', 'url':
        {'view': 'categories', 'arg': 'books'}},
    {'title': 'Фильмы', 'url':
        {'view': 'categories', 'arg': 'movies'}},
    {'title': 'Игры', 'url':
        {'view': 'categories', 'arg': 'games'}},
    {'title': 'Рекомендовать', 'url':
        {'view': None, 'arg': None}}
]

all_posts = Post.objects.all()
last_post = Post.objects.last()
images = Image.objects.all()
last_post_image = Image.objects.last().photo


def index(requests):
    return render(requests, 'main/index.html', context={'title': 'Recommendation',
                                                        'nav_buttons': menu,
                                                        'posts': all_posts,
                                                        'last_post': last_post,
                                                        'last_post_photo': last_post_image,
                                                        'image': images})


def post(requests, username, post):
    return render(requests, 'main/post.html', last_post)


def categories(requests, category):
    # posts = Post.objects.filter()
    # context = {'title': category, }
    return render(requests, 'main/categories.html', context={'category': category})
