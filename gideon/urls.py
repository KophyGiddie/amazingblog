from django.urls import path
from .views import homepage, post_new, post_detail, delete_post, publish_post, unpublish_post, unpublished_posts, edit_post


urlpatterns = [
    path('', homepage),
    path('post_new/', post_new, name='post_new'),
    path('unpublished_posts/', unpublished_posts, name='unpublished_posts'),
    path('posts/<int:article_id>/', post_detail, name='post_detail'),
    path('delete_post/<int:article_id>/', delete_post, name='delete_post'),
    path('publish_post/<int:article_id>/', publish_post, name='publish_post'),
    path('unpublish_post/<int:article_id>/', unpublish_post, name='unpublish_post'),
    path('edit_post/<int:article_id>/', edit_post, name='edit_post'),
]
