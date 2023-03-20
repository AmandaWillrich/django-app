from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): #inherits from UserCreation form
    email = forms.EmailField() #adds this field to the form

    class Meta: #a class that keeps configurations in one place
        model = User #which model it interacts with. It saves in the User Model
        fields = ['username', 'email', 'password1', 'password2']
        #fields to be shown on the form

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ['image']