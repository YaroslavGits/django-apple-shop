from django import forms
from .models import *


class SabscriberForm(forms.ModelForm):
    class Meta():
        model = Sabscriber
        exclude=[""]
