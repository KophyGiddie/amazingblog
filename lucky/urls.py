from django.urls import path
from .views import index, post_new, post_detail


urlpatterns = [
    path('', index),
    path('post_new/', post_new, name='post_new'),
    path('posts/<int:article_id>/', post_detail, name='post_detail'),
]
