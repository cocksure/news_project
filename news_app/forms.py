from django import forms
from .models import Contacts, Comment, News


class NewsUpdateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'body', 'image', 'category', 'status',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'title_ru', 'title_uz', 'title_en', 'slug', 'body', 'body_uz', 'body_en',
                  'body_ru', 'image', 'category', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'title_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'title_en': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'body_uz': forms.Textarea(attrs={'class': 'form-control'}),
            'body_en': forms.Textarea(attrs={'class': 'form-control'}),
            'body_ru': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ['name', 'email', 'message', 'speciality']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']
