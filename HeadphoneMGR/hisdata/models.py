from django.db import models

# Create your models here.
# 헤드폰 이력 조회용 누적 DB table
class HeadphoneHistory(models.Model):
    hh_model = models.CharField(max_length=100)
    hh_serial = models.CharField(max_length=100)
    hh_pDate = models.DateField(null=True)
    hh_pDetail = models.TextField(null=True)
    hh_rDate = models.DateField(null=True)
    hh_rDetail = models.TextField(null=True)
    hh_receiver = models.CharField(max_length=100, null=True)
    hh_checker = models.CharField(max_length=100, null=True)
    hh_state = models.CharField(max_length=100, null=True)