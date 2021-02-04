from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Admin,Farmers,Suppliers,Post

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields =['admin_pic', 'bio']


class NewFarmerForm(forms.ModelForm):
    class Meta:
        model = Admin
        exclude = ('admin',)

class EditFarmerForm(forms.ModelForm):
    class Meta:
        model = Admin
        exclude = ('admin',)

class NewFarmerForm(forms.ModelForm):
    class Meta:
        model = Admin
        exclude = ('user',)


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)

