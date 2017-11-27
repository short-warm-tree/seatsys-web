from django.db import models
class StudentModels(models.Model):
    name = models.CharField(max_length=8)
    stuid = models.CharField(max_length=13)
    weixinid = models.CharField(max_length=100,null=True)
    mm = models.CharField(max_length=6)
    academy=models.CharField(max_length=15,null=True)
    condition = models.BooleanField()
    value=models.IntegerField(default=100)
    breaktimes=models.IntegerField(default=0)
    def __str__(self):
        return self.name
# Create your models here.
