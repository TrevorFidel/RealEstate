from django import forms
from .models import Registration

class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Registration
        fields = ['firstname', 'lastname', 'email', 'password']