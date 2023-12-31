from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['bio']



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields='__all__'

        widgets ={
            'user':forms.TextInput(attrs={'type':'hidden'})
        }
