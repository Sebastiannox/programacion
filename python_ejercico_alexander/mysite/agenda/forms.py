from django import forms
from .models import Agenda
class TableForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = "__all__"
