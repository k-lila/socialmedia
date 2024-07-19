from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ..models import Profile


class ProfileImgForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile image")
    profile_bio = forms.CharField(
        label="bio",
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "bio"}),
    )
    profile_website = forms.CharField(
        label="website",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "website"}
        ),
    )

    class Meta:
        model = Profile
        fields = (
            "profile_image",
            "profile_bio",
            "profile_website",
        )
