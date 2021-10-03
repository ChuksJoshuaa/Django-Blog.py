from django import forms

class Rawschoolform(forms.Form):
    school = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "school"}))
    def clean_school(self, *args, **kwargs):
        school = self.cleaned_data.get("school")
        if "name" == school:
            return "You are welcome"

        else:
            raise forms.ValidationError("Invalid Name!!")
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


