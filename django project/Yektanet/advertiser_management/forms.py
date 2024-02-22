from django import forms
from .models import ad

from django import forms

from django import forms
from .models import ad


class NewForm(forms.ModelForm):
    class Meta:
        model = ad
        fields = ['title', 'advertiser', 'link', 'image']
