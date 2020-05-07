from django.db import models

# Create your models here.
class HeadphoneMain(models.Model):
    hp_model = models.CharField(max_length=100)
    hp_serial = models.CharField(max_length=100)
    hp_pDate = models.DateField(null=True)
    hp_pDetail = models.TextField(null=True)
    hp_rDate = models.DateField(null=True)
    hp_rDetail = models.TextField(null=True)
    hp_receiver = models.CharField(max_length=100, null=True)
    hp_checker = models.CharField(max_length=100, null=True)
    hp_state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.hp_state
    
class History(models.Model):
    h_model = models.CharField(max_length=100)
    h_serial = models.CharField(max_length=100)
    h_pDate = models.DateField(null=True)
    h_pDetail = models.TextField(null=True)
    h_rDate = models.DateField(null=True)
    h_rDetail = models.TextField(null=True)
    h_receiver = models.CharField(max_length=100, null=True)
    h_checker = models.CharField(max_length=100, null=True)
    h_state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.h_state
    