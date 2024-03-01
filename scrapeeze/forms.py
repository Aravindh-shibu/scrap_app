from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from scrapeeze.models import UserProfile,Scrap


class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter username"}),
            "email":forms.TextInput(attrs={"class":"form-control","placeholder":"name@example.com"}),
            "password1":forms.TextInput(attrs={"class":"form-control","placeholder":"Password"}),
            "password2":forms.TextInput(attrs={"class":"form-control","placeholder":"Confirm Password"}),

        }

class SigninForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=('user',)
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "profile_pic":forms.FileInput(attrs={"class":"form-control"}),
        }

class AddForm(forms.ModelForm):
    class Meta:
        model=Scrap
        exclude=("user","status",)

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "category":forms.Select(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "scrap_image":forms.FileInput(attrs={"class":"form-control"}),
            "condition":forms.TextInput(attrs={"class":"form-control"}),
        }