from django import forms
from django.contrib.auth.forms import AuthenticationForm

class loginForm(AuthenticationForm):
    imie = forms.CharField(required=False, label="imie")
    nazwisko = forms.CharField(required=False, label="nazwisko")
    email = forms.CharField(required=False, label="e_mail")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['imie'].widget.attrs.update({'class': 'form-control'})
        self.fields['nazwisko'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})