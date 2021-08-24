from django.db import models
from datetime import datetime
# Create your models here.
class Department(models.Model):   
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return f"Name: {self.name}"

class Employee(models.Model):
    GENDER_CHOICES = [('Male', 'Male'),('Female', 'Female')]  #[(tuple)], ('Male', 'Male') one for desply one male for value
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True, blank = True)
    dob = models.DateField(default = datetime.now, blank = True)
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, default = 'Male', )
    salary = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, null = True)
    photo = models.FileField(upload_to = 'empimage', default = 'empimage/blank.png', blank = True)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
