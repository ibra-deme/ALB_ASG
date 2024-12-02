from django import  forms
from .models import Compagnie

class CompagnieForm(forms.ModelForm):
    class Meta:
        model=Compagnie
        fields="__all__"