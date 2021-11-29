from django.shortcuts import render

from .models import *

menu = [
    {'title': 'Все категории', 'url': '/'},
    {'title': 'Книги', 'url': '/category/books'},
    {'title': 'Фильмы', 'url': '/category/movies'},
    {'title': 'Игры', 'url': '/category/games'},
    {'title': 'Добавить', 'url': 'admin/main/post/'}
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
    read_post = all_posts.get(slug=slug)
    image = read_post.image_set.first()
    return render(requests, 'main/post.html', context={'post': post,
                                                       'image': image,
                                                       'nav_buttons': menu})


def categories(requests, category):
    posts_cat = Post.objects.filter(
        title_post__category__slug=category).order_by('-date_create')
    return render(requests, 'main/categories.html',
                  context={'posts': posts_cat,
                           'nav_buttons': menu})


def user_posts(requests, user):
    print(user)
    user_p = Post.objects.filter(
        user__username=user).order_by('-date_create')
    return render(requests, 'main/categories.html', context={'posts': user_p,
                                                             'nav_buttons': menu})
