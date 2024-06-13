from django import forms
from .models import Transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'type', 'method']
        labels = {
            'amount': 'Miqdori',
            'type': 'Turi',
            'method': 'Usuli'
        }

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='first_name')
    last_name = forms.CharField(max_length=30, required=True, help_text='last_name')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')