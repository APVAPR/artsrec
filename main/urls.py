from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category>/', views.categories, name='categories'),
    path('posts/<str:user>/', views.user_posts, name='user_post'),
    path('post/<slug:slug>/', views.post, name='post')
]
