from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
