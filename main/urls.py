from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category>/', views.categories, name='categories'),
    path('post/<str:username>/<slug:post>/', views.post, name='post')
]
