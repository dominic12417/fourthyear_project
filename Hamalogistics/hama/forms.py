from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from django import forms
from datetime import date

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields ='__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class vehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields='__all__'

class bookvehicleForm(ModelForm):
    class Meta:
        model=Book_Vehicle
        fields='__all__'
