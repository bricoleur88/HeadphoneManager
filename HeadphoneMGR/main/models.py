from django.db import models

# Create your models here.
class HeadphoneMain(models.Model):
    hp_model = models.CharField(max_length=100)
    hp_serial = models.CharField(max_length=100)
    hp_pDate = models.DateField()
    hp_pDetail = models.TextField()
    hp_rDate = models.DateField()
    hp_rDetail = models.TextField()
    hp_receiver = models.CharField(max_length=100)
    hp_checker = models.CharField(max_length=100)
    hp_state = models.CharField(max_length=100)

