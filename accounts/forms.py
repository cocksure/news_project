from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput
from accounts.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'})
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password_2 = forms.CharField(label='Повторите пароль',
                                 widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот электронный адрес уже используется')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Это имя пользователя уже используется')
        return username

    def clean_password_2(self):
        data = self.cleaned_data
        if data['password'] != data['password_2']:
            raise forms.ValidationError('Пароли не совпатают!')

        return data['password_2']


class UserEditForms(forms.ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Год рождения', widget=forms.DateInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(label='Фото', required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
