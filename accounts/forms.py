from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    SKILLS_CHOICES = (
        ('1', 'HTML'),
        ('2', 'Css'),
        ('3', 'Javascript'),
        ('4', 'Ajax'),
        ('5', 'PHP, .Net, Python'),
    )
    skills= forms.MultipleChoiceField(choices=SKILLS_CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Profile
        fields = ('phone', 'profession', 'skills', 'experience', 'hourly_rate', 'total_project', 'english_level', 'availability', 'bio')