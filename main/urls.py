from django.urls import path

from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('post/<str:name>/<slug:post>/', views.post, name='post')
]
