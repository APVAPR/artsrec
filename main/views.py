from django.shortcuts import render

from .models import *

menu = [
    {'title': 'На главную', 'url':
        {'view': 'index', 'arg': ''}},
    {'title': 'Книги', 'url':
        {'view': 'categories', 'arg': 'books'}},
    {'title': 'Фильмы', 'url':
        {'view': 'categories', 'arg': 'movies'}},
    {'title': 'Игры', 'url':
        {'view': 'categories', 'arg': 'games'}},
    {'title': 'Рекомендовать', 'url':
        {'view': None, 'arg': None}}
]

all_posts = Post.objects.all().order_by('-date_create')
last_post = all_posts.first()
images = Image.objects.all()
last_post_image = Image.objects.last().photo



def index(requests):

    context = {'title': 'Recommendation',
               'nav_buttons': menu,
               'posts': all_posts,
               'last_post': last_post,
               'last_post_photo': last_post_image,
               'images': images}

    return render(requests, 'main/index.html', context=context)


def post(requests, slug):
    post = all_posts.get(slug=slug)
    image = post.image_set.first()
    return render(requests, 'main/post.html', context={'post': post, 'image': image})


def categories(requests, category):
    posts_cat = Post.objects.filter(title_post__category__title=category)

    return render(requests, 'main/categories.html',
                  context={'posts_cat': posts_cat,
                           'nav_buttons': menu})
