import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# FOR BLOG FRAMEWORK
class Post(models.Model):
    title = models.CharField(max_length=333)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)

    body = models.TextField(max_length=100000)

    def __str__(self):
        return self.title

    def published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Music(models.Model):
    track_title = models.CharField(max_length=333)
    album_artist = models.CharField(max_length=333)
    album_title = models.CharField(max_length=333)

    def __str__(self):
        return self.track_title + '-' + self.album_artist

class Product_recommend(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, default='Product Placeholder')
    amazon_link = models.CharField(max_length=65535, default='https://www.amazon.com/')
