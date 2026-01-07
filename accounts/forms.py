from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Логін',
            'email': 'Email',
        }
        help_texts = {
            'username': '',
            'email': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Ваш логін'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'you@example.com'
            }),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'birth_date']
        labels = {
            'bio': 'Коротко про себе',
            'avatar': 'Аватар',
            'birth_date': 'Дата народження',
        }
        help_texts = {
            'bio': '',
            'avatar': '',
            'birth_date': '',
        }
        widgets = {
            'bio': forms.Textarea(attrs={
                'placeholder': 'Розкажіть трохи про себе...',
                'rows': 3,
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }
