from django.db import models
from django import forms
from .models import StudentForm
COUNTRY_CHOICES=[
    ('nepal','Nepal'), ('bangladesh','Bangladesh'), ('bhutan','Bhutan'),
     ('india','India'), ('maldives','Maldives'), ('pakistan','Pakistan'), ('sri Lanka','Sri Lanka'),
]
COUNTRY_CODE_CHOICES=[
    ('nepal','Nepal(+977)'), ('bangladesh','Bangladesh(+880)'), ('bhutan','Bhutan(+975)'),
     ('india','India(+91)'), ('maldives','Maldives(+960)'), ('pakistan','Pakistan(+92)'), 
     ('sri Lanka','Sri Lanka(+84)'),
]

FACULTY_CHOICES=[
('Engineering','Institute of Engineering'),('Medicine','Institute of Medicine'),('Forestry','Institute of Forestry'),
('Agriculture','Institute of Agriculture and Animal Science'),('Science','Institute of Science and Technology'),('Law','Faculty of Law'),
('Humanities','Faculty of Humanities and Social Studies'),('Management','Faculty of Management'),('Education','Faculty of Education'),

]

EVALUATION_CHOICES=[
    ('O','Outstanding'),('E','Excellent'),('G','Good'),
    ('S','Satisfactory'),('P','Pass'),('F','Fail'),
]
class StudentF(forms.ModelForm):
    class Meta:
        model=StudentForm
        fields='__all__'
        widgets = {
        'std_id': forms.NumberInput(attrs={"placeholder":"Student ID"}),
            'first_name': forms.TextInput(attrs={"placeholder":"Your First Name"}),
            'middle_name': forms.TextInput(attrs={"placeholder":"Your Middle Name"}),
            'last_name': forms.TextInput(attrs={"placeholder":"Your Last Name"}),
            'city': forms.TextInput(attrs={"placeholder":"Your City"}),
            'country': forms.Select(choices=COUNTRY_CHOICES),
            'country_code':forms.Select(choices=COUNTRY_CODE_CHOICES),
            'phone_number': forms.NumberInput(attrs={"placeholder":" Your Phonenumber","class":"phone_number"}),
            'faculty': forms.Select(choices=FACULTY_CHOICES),
            'marks_obtained': forms.TextInput(attrs={"placeholder":"Your Obtained Marks"}),
            'percentage': forms.NumberInput(attrs={"placeholder":"Your Obtained Percentage"}),
            'evaluation': forms.Select(choices=EVALUATION_CHOICES)
    }