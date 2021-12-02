from django.urls import path
from django.contrib.auth.views import LogoutView
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('category/<slug:category>/', views.categories, name='categories'),
    path('posts/<str:user>/', views.user_posts, name='user_post'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('add-post/', views.add_post, name='add_post')
]
