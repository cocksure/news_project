from django import forms
from .models import Contacts, News, Comment


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ['name', 'email', 'message', 'speciality']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']
