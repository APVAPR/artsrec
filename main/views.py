from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django import views
from django.shortcuts import render, redirect

from .models import Post, Image, Item
from .forms import LoginForm, RegistrationForm, PostForm, ItemForm, ImageForm
from django.contrib.auth import authenticate, login

from main.utils import get_slug

menu = [
    {'title': 'Все категории', 'url': '/'},
    {'title': 'Книги', 'url': '/category/books'},
    {'title': 'Фильмы', 'url': '/category/movies'},
    {'title': 'Игры', 'url': '/category/games'}
]


def index(requests):
    all_posts = Post.objects.all().order_by('-date_create')
    images = Image.objects.all()
    context = {'title': 'Recommendation',
               'nav_buttons': menu,
               'posts': all_posts,
               'images': images}

    return render(requests, 'main/index.html', context=context)


class LoginView(views.View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'main/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                print(user)
                return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'main/login.html', context)


class RegistrationView(views.View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'main/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
            )
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            if form.cleaned_data['first_name']:
                new_user.first_name = form.cleaned_data['first_name']
            if form.cleaned_data['last_name']:
                new_user.last_name = form.cleaned_data['last_name']
            new_user.is_staff = True
            new_user.save()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'main/registration.html', context)


def get_full_post(requests, user, slug):
    read_post = Post.objects.get(title_post__slug=slug)
    image = read_post.image_set.first()
    return render(requests, 'main/post.html', context={'post': read_post,
                                                       'image': image,
                                                       'nav_buttons': menu})


def categories(requests, category):
    posts_cat = Post.objects.filter(
        title_post__category__slug=category).order_by('-date_create')
    return render(requests, 'main/categories.html',
                  context={'posts': posts_cat,
                           'nav_buttons': menu})


def user_posts(requests, user):
    user_p = Post.objects.filter(
        user__username=user).order_by('-date_create')
    return render(requests, 'main/categories.html', context={'posts': user_p,
                                                             'nav_buttons': menu})


class AddPostView(LoginRequiredMixin, views.View):

    def get(self, request, *args, **kwargs):
        post_form = PostForm(request.POST or None)
        item_form = ItemForm(request.POST or None)
        context = {
            'post_form': post_form,
            'item_form': item_form
        }
        return render(request, 'main/add_post.html', context)

    def post(self, request, *args, **kwargs):
        post_form = PostForm(request.POST or None)
        item_form = ItemForm(request.POST or None)
        if post_form.is_valid() and item_form.is_valid():
            item = Item.objects.create(
                title=item_form.cleaned_data['title'],
                author=item_form.cleaned_data['author'],
                category=item_form.cleaned_data['category'],
                slug=get_slug(item_form.cleaned_data['author'],
                              item_form.cleaned_data['title'])
            )
            Post.objects.create(user=request.user,
                                title_post=item,
                                content=post_form.cleaned_data['content'],
                                )
        return redirect('add_image')


class AddImageView(LoginRequiredMixin, views.View):

    def get(self, request, *args, **kwargs):
        image_form = ImageForm(request.POST or None, request.FILES or None)
        context = {
            'image_form': image_form,
        }
        return render(request, 'main/add_image.html', context)

    def post(self, request, *args, **kwargs):
        image_form = ImageForm(request.POST or None, request.FILES or None)
        if image_form.is_valid():
            image_form.save()
        return redirect('index')
