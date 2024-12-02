from django import  forms
from .models import Vol

class VolForm(forms.ModelForm):
    class Meta:
        model=Vol
        fields = '__all__'