from django.db import models

# Create your models here.

class Category (models.Model): 
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=10)


    def __str__(self):
        return self.name



class Doctor (models.Model): 
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, related_name='doctors', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
