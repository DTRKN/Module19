from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="Введите логин",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        min_length=8,
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    repeat_password = forms.CharField(
        min_length=8,
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    age = forms.CharField(
        max_length=3,
        label="Введите свой возраст",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    ) 