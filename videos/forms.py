from django import forms
from .models import Video, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['title', 'description', 'thumbnail', 'video']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']