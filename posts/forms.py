from django import forms
from .models import postmode
from django.urls import reverse
class post_form(forms.ModelForm):
    class Meta:
        model = postmode
        fields = [
            'title',
            'content'
        ]
