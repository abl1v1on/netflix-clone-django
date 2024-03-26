from django import forms

from .models import Profile


class CreateNewProfileForm(forms.ModelForm):
    name = forms.CharField(label='Название профиля',
                           widget=forms.TextInput(attrs={
                               'class': 'p-2 bg-gray-500 rounded-sm text-gray-200 outline-none block w-full',
                               'placeholder': 'Введите название профиля'
                           }))

    class Meta:
        model = Profile
        fields = ('name', 'age_limit')
