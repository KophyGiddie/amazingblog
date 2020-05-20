from django.db import models
from users.models import BlogUser


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    category = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-published_date', )


class PostComment(models.Model):
    author = models.ForeignKey(BlogUser, related_name='comments', on_delete=models.SET_NULL, blank=True, null=True)
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.comment
