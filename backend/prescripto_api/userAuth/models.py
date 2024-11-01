from django.db import models

# Create your models here.

class DemoUser (models.Model) : 
    user_name = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=8)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.user_name
