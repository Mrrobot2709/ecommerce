from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField()
    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email