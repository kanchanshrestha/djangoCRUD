from django.db import models

class TeacherForm(models.Model):
    emp_id=models.IntegerField()
    first_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    street=models.IntegerField()
    phone_number=models.CharField(max_length=255)
    country_code=models.CharField(max_length=30,null=True,blank=True)
    subject=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    salary=models.BigIntegerField()
    