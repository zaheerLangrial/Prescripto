from django.db import models

# Create your models here.
class NavbarItems (models.Model): 
    title = models.CharField(max_length=20)
    url = models.CharField(max_length=20)

    def __str__(self):
        return self.title
