from django.db import models

# Create your models here.

class Dabang(models.Model):
    const_date = models.CharField(max_length=100, verbose_name='준공년월')
    price = models.PositiveIntegerField(verbose_name='가격')
    address = models.CharField(max_length=50, verbose_name='주소')
    space = models.CharField(max_length=10, verbose_name='면적')
    construction_firm = models.CharField(max_length=20, verbose_name='건설사')
    low_high = models.CharField(max_length=10, verbose_name='저/고층')
    household = models.PositiveSmallIntegerField(verbose_name='세대주')
