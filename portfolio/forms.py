from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'