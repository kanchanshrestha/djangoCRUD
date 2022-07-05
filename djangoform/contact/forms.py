from django.db import models
from django import forms
from .models import ContactForm

DEPARTMENT_CHOICES=[
     ('IT','Information Technology'),('MGT','Management'), ('PBH' , 'Public Health'),
    ('PYS', 'Physics'), ('CHEM' ,'Chemistry'),('ZOO','Zoology'), ('BOT','Botany'),
    ('POP','Polpulation')

    ]
class ContactF(forms.ModelForm):
    class Meta:
        model=ContactForm
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={"placeholder":"Your Name"}),
            'email_address':forms.EmailInput(attrs={"palceholder":"Your Email Address"}),
            'phone_numebr':forms.NumberInput(attrs={"placeholder":"Your Contact Number"}),
            'department':forms.Select(choices=DEPARTMENT_CHOICES),
            'message':forms.TextInput(attrs={"placeholder":"Please Type Your Message"})
        }
