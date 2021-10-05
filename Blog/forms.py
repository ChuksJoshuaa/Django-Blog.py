from django import forms

from .models import Article

class Articleform(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "details",
            "items",
            "price"
        ]


class RawArticleform(forms.Form):
    First_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter First_name",
        "rows": 5,
        "cols": 10
    }))

    Last_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter Last_name",
        "rows": 5,
        "cols": 10
    }))

    Email = forms.EmailField()

    def clean_Email(self):

        Email = self.cleaned_data.get("Email")

        if ".com" in Email:
            return Email

        elif ".ng" in Email:
             return Email

        else:
            raise forms.ValidationError("Invalid input, Try again!!")


    Password = forms.CharField(widget=forms.PasswordInput(attrs={"label": "Enter Password"}))

    def clean_Password(self, *args, **kwargs):
        Password = self.cleaned_data.get("Password")
        number = 5
        if len(Password) > number:
            return Password

        else:
            raise forms.ValidationError("Your password must be atleast 8 characters !!")









