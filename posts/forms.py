from django import forms
from .models import postmode, Comment, PostComment
from django.urls import reverse
class post_form(forms.ModelForm):
    class Meta:
        model = postmode
        fields = [
            'title',
            'content'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }