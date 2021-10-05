from .models import sapamode
from django import forms


class sapaform(forms.ModelForm):
    class Meta:
        model = sapamode
        fields = [
            "title",
            "image",
            "content"
        ]



class Rawsapaform(forms.Form):
    First_name = forms.CharField(widget=forms.TextInput(attrs={"Label": "Enter First_name"}))
    Last_name = forms.CharField(widget=forms.TextInput(attrs={"Label": "Enter Last_name"}))
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput(attrs={"Label": "Enter Password"}))
