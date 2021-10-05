from django import forms
from .models import game

class gameform(forms.ModelForm):
    class Meta:
        model = game
        fields = [
            'server',
            'gametype',
            'price'
        ]


class Rawgameform(forms.Form):
    email = forms.EmailField()
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if "edu" not in email:
            raise forms.ValidationError("This is a wrong email, try again! ")

        else:
            return email

    title = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "your name"}))
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')

        if "name" not in title:
            return forms.ValidationError("This is not a valid name! ")
        else:
            return title

    description = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "your description",
        "rows": 12,
        "cols": 59,
        "class": "your-class-for-textarea",
        "id": "my-id-for-textarea"}
      )
    )
    price = forms.DecimalField(initial=200.23)



