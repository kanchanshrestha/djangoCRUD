from django.db import models

class StudentForm(models.Model):
    std_id=models.IntegerField()
    first_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    phone_number=models.BigIntegerField()
    faculty=models.CharField(max_length=255)
    marks_obtained=models.IntegerField()
    percetage=models.IntegerField
    evaluation=models.CharField(max_length=255)
    

    
    
