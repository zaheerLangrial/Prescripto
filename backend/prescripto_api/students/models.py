from django.db import models

# Create your models here.


class Student (models.Model) : 
    stu_name = models.CharField(max_length=30)
    roll_number = models.IntegerField(max_length=10, unique=True)
    level = models.IntegerField(max_length=10)
    father_name = models.CharField(max_length=30)
    section = models.CharField(max_length=10)


    def __str__(self):
        return self.stu_name
