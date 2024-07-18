from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ..models import Profile


class ProfileImgForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile image")

    class Meta:
        model = Profile
        fields = ("profile_image",)
