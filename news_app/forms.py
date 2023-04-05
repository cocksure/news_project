from django import forms
from .models import Contacts


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ['name', 'email', 'message', 'speciality']
