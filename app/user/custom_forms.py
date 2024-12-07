from cProfile import label

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Patient


class CustomUserCreationForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm = forms.CharField(label='Confirm', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = Patient
        fields = ('first_name', 'last_name', 'email', 'password')

    def is_valid(self):
        valid = super().is_valid()

        if valid:
            if self.cleaned_data.get('password') != self.cleaned_data.get('confirm'):
                self.add_error('confirm', 'Passwords must match')
                return False
        return valid
