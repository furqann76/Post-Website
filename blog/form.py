from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Profile
from .models import Comment


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
            profile.phone_number = self.cleaned_data["phone_number"]
            profile.profile_pic = self.cleaned_data["profile_pic"]
            profile.address = self.cleaned_data["address"]
            profile.save()

        return user


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["phone_number", "address", "profile_pic"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Write your comment..."}
            ),
        }
