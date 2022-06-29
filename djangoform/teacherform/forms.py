from django.db import models
from django import forms
from .models import TeacherForm

STREET_CHOICES= [
    ('1','01'), ('2','02'),('3','03'),('4','04'),('5','05'),('6','06'),('7','07'),('8','08'),('9','09'),('10','10'),
     ('11','11'), ('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),
      ('21','21'), ('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),
       ('31','31'), ('32','32'),
    ]

DEPARTMENT_CHOICES=[
     ('IT','Information Technology'),('M','Management'), ('PB' , 'Public Health'),
    ('PY', 'Physics'), ('C' ,'Chemestry'),('Z','Zoology'), ('B','Botany'),
    ('PO','Polpulation')

    ]
COUNTRY_CHOICES=[
    ('nepal','Nepal'), ('bangladesh','Bangladesh'), ('bhutan','Bhutan'),
     ('india','India'), ('maldives','Maldives'), ('pakistan','Pakistan'), ('sri Lanka','Sri Lanka'),
]
COUNTRY_CODE_CHOICES=[
    ('nepal','Nepal(+977)'), ('bangladesh','Bangladesh(+880)'), ('bhutan','Bhutan(+975)'),
     ('india','India(+91)'), ('maldives','Maldives(+960)'), ('pakistan','Pakistan(+92)'), 
     ('sri Lanka','Sri Lanka(+84)'),
]
class TeacherF(forms.ModelForm):
    class Meta:
        model=TeacherForm
        fields='__all__'
        widgets = {
            'emp_id': forms.NumberInput(attrs={"placeholder":"Employee ID"}),
            'first_name': forms.TextInput(attrs={"placeholder":"Your First Name"}),
            'middle_name': forms.TextInput(attrs={"placeholder":"Your Middle Name"}),
            'last_name': forms.TextInput(attrs={"placeholder":"Your Last Name"}),
            'city': forms.TextInput(attrs={"placeholder":"Your City"}),
            'country': forms.Select(choices=COUNTRY_CHOICES),
            'street': forms.Select(choices=STREET_CHOICES),
            'country_code':forms.Select(choices=COUNTRY_CODE_CHOICES),
            'phone_number': forms.NumberInput(attrs={"placeholder":" Your Phonenumber","class":"phone_number"}),
            'subject': forms.TextInput(attrs={"placeholder":"Your Subject"}),
            'department': forms.Select(choices=DEPARTMENT_CHOICES),
            'salary': forms.NumberInput(attrs={"placeholder":"Your Salary"})
        }