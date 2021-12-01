from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('category/<slug:category>/', views.categories, name='categories'),
    path('posts/<str:user>/', views.user_posts, name='user_post'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('add-post/', views.add_post, name='add_post')
]
