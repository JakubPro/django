from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    error_messages = {
        'password_mismatch': 'Hasła muszą być takie same, spróbuj ponownie.',
        'password_too_common': 'Proszę, wybierz silniejsze hasło.',
        'password_entirely_numeric': 'Hasło nie może składać się tylko z cyfr.',
        'password_length': 'Hasło musi mieć co najmniej 8 znaków.',
        'password_similar': 'Hasło nie może być zbyt podobne do innych informacji.',
    }
