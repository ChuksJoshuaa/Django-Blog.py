from django.contrib import admin
from .models import postmode, Comment, PostComment
# Register your models here.

admin.site.register(postmode)
admin.site.register(Comment)
admin.site.register(PostComment)


