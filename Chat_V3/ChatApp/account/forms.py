from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     return cd['password2']
    
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
   
    email = forms.EmailField() 
 
   
class ProfileUpdateForm(forms.ModelForm):   
    class Meta:   
        model = Profile
        fields = ['image']
    
