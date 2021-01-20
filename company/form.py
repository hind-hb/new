from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee
from django.forms import ModelForm


class signUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput)

    class Meta:
        model=User
        fields ={'username','email','password1','password2'}

class NewEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name,address,department,date']
