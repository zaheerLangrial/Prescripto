from django.db import models

# Create your models here.


# sab se pehla kam model banana then fir or kuch jo jo hamy chahiyee us hesab se model ban jye ga

class DemoUser (models.Model) : 
    user_name = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=8)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        # yeh cheez ha admin interface k liye k odr kis cheez se isy represent karna
        return self.user_name
