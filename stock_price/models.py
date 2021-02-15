
from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class NIKKEI(models.Model):
    date = models.DateField(verbose_name='日付',null=True,default=datetime.now)
    high = models.FloatField(verbose_name='高値',null=True)
    low = models.FloatField(verbose_name='安値',null=True)
    open = models.FloatField(verbose_name='始値',null=True)
    close = models.FloatField(verbose_name='終値',null=True)
    volume = models.FloatField(verbose_name='出来高',null=True)
    #adjclose = models.IntegerField(verbose_name='',)

class SP500(models.Model):
    date = models.DateField(verbose_name='日付',null=True,default=datetime.now)
    high = models.FloatField(verbose_name='高値',null=True)
    low = models.FloatField(verbose_name='安値',null=True)
    open = models.FloatField(verbose_name='始値',null=True)
    close = models.FloatField(verbose_name='終値',null=True)
    volume = models.FloatField(verbose_name='出来高',null=True)
    #adjclose = models.IntegerField(verbose_name='',)

class USDJPY(models.Model):
    date = models.DateField(verbose_name='日付',null=True,default=datetime.now)
    high = models.FloatField(verbose_name='高値',null=True)
    low = models.FloatField(verbose_name='安値',null=True)
    open = models.FloatField(verbose_name='始値',null=True)
    close = models.FloatField(verbose_name='終値',null=True)
    volume = models.FloatField(verbose_name='出来高',null=True)
    #adjclose = models.IntegerField(verbose_name='',)

class BITCOIN(models.Model):
    date = models.DateField(verbose_name='日付',null=True,default=datetime.now)
    high = models.FloatField(verbose_name='高値',null=True)
    low = models.FloatField(verbose_name='安値',null=True)
    open = models.FloatField(verbose_name='始値',null=True)
    close = models.FloatField(verbose_name='終値',null=True)
    volume = models.FloatField(verbose_name='出来高',null=True)
    #adjclose = models.IntegerField(verbose_name='',)

class COMMON(models.Model):
    date = models.DateField(verbose_name='日付',null=True,default=datetime.now)
    nikkei = models.FloatField(verbose_name='日経225', null=True)
    sp500 = models.FloatField(verbose_name='S&P500', null=True)
    usdjpy = models.FloatField(verbose_name='USD/JPY', null=True)
    bitcoin = models.FloatField(verbose_name='BITCOIN', null=True)
