from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


class LogInUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={
                                   'class': 'p-2 bg-gray-200 rounded-sm text-gray-900 outline-none block w-full',
                                   'placeholder': 'Введите логин'
                               }))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'p-2 bg-gray-200 rounded-sm text-gray-900 outline-none block w-full',
                                   'placeholder': 'Введите пароль'
                               }))


class SignUpUserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'p-2 bg-gray-200 rounded-sm text-gray-900 outline-none block w-full',
                                       'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(label='Электронная почта',
                             widget=forms.EmailInput(
                                 attrs={
                                     'class': 'p-2 bg-gray-200 rounded-sm text-gray-900 outline-none block w-full',
                                     'placeholder': 'Введите email'
                                 }
                             ))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'p-2 bg-gray-200 rounded-sm text-gray-900 outline-none block w-full',
                                        'placeholder': 'Введите пароль'
                                    }
                                ))
    password2 = forms.CharField(label='Подтвердите пароль',
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'p-2 bg-gray-200 rounded-sm text-gray-900 outline-none block w-full',
                                        'placeholder': 'Подтвердите пароль'
                                    }
                                ))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким Email-ом уже существует')
        return email

    def clean_password1(self):
        password = self.cleaned_data['password1']
        if str(password).isdigit():
            raise ValidationError('Пароль не должен состоять только из цифр')
        return password
