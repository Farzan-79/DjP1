from django import forms
from .models import UserProfile

class ProfileCompletionForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'bio', 'email', 'picture']
