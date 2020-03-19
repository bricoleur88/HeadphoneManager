from django.db import models

# Create your models here.

class User(models.Model):
    u_name = models.CharField(max_length=100)
    u_division = models.CharField(max_length=100)
    
    def __str__(self):
        return self.u_name