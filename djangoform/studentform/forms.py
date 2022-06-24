from django import forms
from .models import StudentForm

class StudentF(forms.ModelForm):
    class Meta:
        model=StudentForm
        fields='__all__'