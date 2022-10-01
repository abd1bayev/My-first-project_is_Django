from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Fikr-mulohaza shakli"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")