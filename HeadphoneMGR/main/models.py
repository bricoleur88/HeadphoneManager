from django.db import models

# Create your models here.
class HeadphoneMain(models.Model):
    hp_model = models.CharField(max_length=100, verbose_name="모델명")
    hp_serial = models.CharField(max_length=100, verbose_name="일련번호")
    hp_pDate = models.DateField(null=True, verbose_name="지급일")
    hp_pDetail = models.TextField(null=True, verbose_name="지급내용")
    hp_rDate = models.DateField(null=True, verbose_name="반납일")
    hp_rDetail = models.TextField(null=True, verbose_name="반납내용")
    hp_receiver = models.CharField(max_length=100, null=True, verbose_name="인수자")
    hp_checker = models.CharField(max_length=100, null=True, verbose_name="확인자")
    hp_state = models.CharField(max_length=100, verbose_name="상태")
    
    def __str__(self):
        return self.hp_state
    
class History(models.Model):
    h_model = models.CharField(max_length=100, verbose_name="모델명")
    h_serial = models.CharField(max_length=100, verbose_name="일련번호")
    h_pDate = models.DateField(null=True, verbose_name="지급일")
    h_pDetail = models.TextField(null=True, verbose_name="지급내용")
    h_rDate = models.DateField(null=True, verbose_name="반납일")
    h_rDetail = models.TextField(null=True, verbose_name="반납내용")
    h_receiver = models.CharField(max_length=100, null=True, verbose_name="인수자")
    h_checker = models.CharField(max_length=100, null=True, verbose_name="확인자")
    h_state = models.CharField(max_length=100, verbose_name="상태")
    
    def __str__(self):
        return self.h_state
    