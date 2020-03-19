from django.db import models

# Create your models here.

class Headphone(models.Model):
    h_name = models.CharField(max_length=100)
    h_serial = models.CharField(max_length=100)
    
    def __str__(self):
        return self.h_name
    

    
    