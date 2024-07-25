from django import forms
from ..models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        max_length=140,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Escreva seu post",
                "class": "form-control post-form__form",
            }
        ),
        label="",
    )

    class Meta:
        model = Post
        exclude = ("user", "likes")
