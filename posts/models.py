from django.urls import reverse
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class postmode(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"id": self.id})

class Comment(models.Model):
    post = models.ForeignKey(postmode, on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return 'Comment {}'.format(self.commenter_name)


class PostComment(models.Model):
    sno = models.AutoField(primary_key=True)




