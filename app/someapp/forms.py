from django import forms

from .models import Huuser

class PostHuuserForm(forms.ModelForm):
    class Meta: 
        model = Huuser
        fields = ("first_name", "last_name")