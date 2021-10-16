from django import forms
from .models import postmode, Comment, PostComment
from django.urls import reverse
class post_form(forms.ModelForm):
    class Meta:
        model = postmode
        fields = [
            'title',
            'image',
            'content'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment_body'].widget.attrs.update({
            'autocomplete': 'off'
        })