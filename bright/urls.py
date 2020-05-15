from django.urls import path
from .views import homepage, post_new, post_detail, post_delete, publish_post


urlpatterns = [
    path('', homepage),
    path('post_new/', post_new, name='post_new'),
    path('posts/<int:article_id>/', post_detail, name='post_detail'),
    path('post_delete/<int:article_id>/', post_delete, name='post_delete'),
    path('publish_post/<int:article_id>/', publish_post, name='publish_post'),
]
