from django import forms
from .models import school


class schoolform(forms.ModelForm):
    class Meta:
         model = school
         fields = [
            "price",
            "location",
            "description"
         ]


class Rawschoolform(forms.Form):
    school = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "school"}))
    summary = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "summary",
        "rows": 10,
        "cols": 40,
    }))

    email = forms.EmailField()
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if "edu" not in email:
            raise forms.ValidationError("You entered an incorrect input")

        else:
            return email
    price = forms.DecimalField(initial=10.22)





