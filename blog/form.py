from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    profile_pic = forms.ImageField(required=False)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone_number",
            "password1",
            "password2",
            "profile_pic",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user.profile.phone_number = self.cleaned_data["phone_number"]
            user.profile.profile_pic = self.cleaned_data["profile_pic"]
            user.profile.save()
        return user
