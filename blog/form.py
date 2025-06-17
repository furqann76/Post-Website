from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Profile
from blog.signals import post_save
from django.dispatch import receiver


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    profile_pic = forms.ImageField(required=True, label="Profile Picture")
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255, widget=forms.Textarea)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()  # This triggers the signal to create a profile
            profile = user.profile
            # Now just update the existing profile
            """profile = Profile.objects.get(user=user)"""
            profile.phone_number = self.cleaned_data["phone_number"]
            profile.profile_pic = self.cleaned_data["profile_pic"]
            profile.save()

        return user
