from django.db import models
from django import forms
from .models import TeacherForm


class TeacherF(forms.ModelForm):
    class Meta:
        model=TeacherForm
        fields='__all__'