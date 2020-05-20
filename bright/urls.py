from django.urls import path
from .views import homepage, post_new, post_detail, post_delete, publish_post,unpublish_post,edit_post,unpublished_posts


urlpatterns = [
    path('', homepage),
    path('post_new/', post_new, name='post_new'),
    path('posts/<int:article_id>/', post_detail, name='post_detail'),
    path('post_delete/<int:article_id>/', post_delete, name='post_delete'),
    path('publish_post/<int:article_id>/', publish_post, name='publish_post'),
    path('unpublish_post/<int:article_id>/', unpublish_post, name='unpublish_post'),
    path('edit_post/<int:article_id>/', edit_post, name='edit_post'),
    path('unpublished_posts/', unpublished_posts, name='unpublished_posts'),
]
