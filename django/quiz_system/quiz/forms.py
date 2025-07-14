from django import forms
from .models import User, Quiz, Question
from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password', 'role']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quiz', 'text', 'option1', 'option2', 'option3', 'option4', 'correct_option']

class EditProfileForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput, required=False, label="New Password"
    )

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password']
