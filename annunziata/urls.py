
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]