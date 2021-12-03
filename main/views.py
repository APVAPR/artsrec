from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post, Image
from .forms import LoginForm, RegistrationForm, AddPostForm
from django.contrib.auth import authenticate, login

menu = [
    {'title': 'Все категории', 'url': '/'},
    {'title': 'Книги', 'url': '/category/books'},
    {'title': 'Фильмы', 'url': '/category/movies'},
    {'title': 'Игры', 'url': '/category/games'}
]

all_posts = Post.objects.all().order_by('-date_create')
images = Image.objects.all()

def index(requests):
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
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
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
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'main/registration.html', context)


def post(requests, slug):
    read_post = all_posts.get(slug=slug)
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


def add_post(requests):
    if requests.method == 'POST':
        form = AddPostForm(requests.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostForm()
    return render(requests, 'main/add_post.html', context={'nav_buttons': menu, 'form': form})
