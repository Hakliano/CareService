from django import forms
from .models import Partner, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'address', 'phone', 'email', 'category']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_content']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'review_content': forms.Textarea(attrs={'rows': 3}),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']