from django.db import models

class StudentForm(models.Model):
    std_id=models.IntegerField()
    first_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    phone_number=models.IntegerField()
    country_code=models.CharField(max_length=30,null=True,blank=True)
    faculty=models.CharField(max_length=255)
    marks_obtained=models.IntegerField()
    percentage=models.FloatField(null=True,blank=True)
    evaluation=models.CharField(max_length=255)
    

    
    
