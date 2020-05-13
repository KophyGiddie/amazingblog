from django.urls import path
from .views import homepage, post_new, post_detail


urlpatterns = [
    path('', homepage),
    path('post_new/', post_new, name='post_new'),
    path('posts/<int:article_id>/', post_detail, name='post_detail'),
]
