from django import forms

from .models import  employees

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class employeesFORM(ModelForm):
     class Meta:
         model = employees
         fields = '__all__'
