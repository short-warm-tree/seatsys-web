from django.db import models
from login.models import StudentModels


# Create your models here.
class polling(models.Model):
    trigger_time = models.CharField(max_length=14)#触发时间
    owner_id = models.TextField(default = 0)
    source_id = models.TextField(default = 0)
    order = models.IntegerField(default = 0)
    status = models.CharField(max_length = 1)
    seat_id = models.CharField(max_length = 5,default = '0000')
    def __str__(self):
        return self.trigger_time
    class Meta:
        ordering = ['-status','trigger_time']
class auto_token(models.Model):
    access_token = models.TextField(default = 0)
    begin_time = models.CharField(max_length=14)
    end_time = models.CharField(max_length=14)
    token_status = models.CharField(max_length=1)
    def __str__(self):
        return self.access_token
    class Meta:
        ordering = ['-token_status','begin_time']
class seat(models.Model):
    SEATSTATUS_CHOICES = {
        ('1', '空闲'),
        ('2', '已预约'),
        ('3', '使用中'),
        ('4', '暂离'),
    }
    SEATLEVEL_CHOICES = {
        ('1', '1楼'),
        ('2', '2楼'),
        ('3', '3楼'),
        ('4', '4楼'),
        ('5', '5楼'),
    }
    seatid = models.CharField(max_length=5, default='0000', )
    seatlevel = models.CharField(max_length=1,default='1',choices=SEATLEVEL_CHOICES)
    seatstatus = models.CharField(max_length=5, default='1',choices=SEATSTATUS_CHOICES, )
    def __str__(self):
        return self.seatid
    class Meta:
        ordering = ['seatid']
class orderrecord(models.Model):
    ORDERSTATUS_CHOICES =  {
        ('1','未在生效中'),
        ('2','生效中'),
        ('3','过期'),
        ('4','过渡期')
    }

    # 外键与其他的表相连
    student = models.ForeignKey(StudentModels,default='')
    seat = models.ForeignKey(seat,default='')
    orderid = models.CharField(max_length=20, default='', )


    fromtime = models.TimeField(default='',)
    timelong = models.CharField(default='',max_length=5,)
    orderstatus = models.CharField(max_length=5,default='1',choices=ORDERSTATUS_CHOICES,)
    def __str__(self):
        return self.orderid

# Create your models here.
