from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import UserModel


class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Passwords do not match')
        return self.cleaned_data
