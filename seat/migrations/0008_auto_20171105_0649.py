# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0007_auto_20171105_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto_token',
            name='access_token',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='orderstatus',
            field=models.CharField(choices=[('4', '过渡期'), ('3', '过期'), ('2', '生效中'), ('1', '未在生效中')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatlevel',
            field=models.CharField(choices=[('1', '1楼'), ('4', '4楼'), ('3', '3楼'), ('5', '5楼'), ('2', '2楼')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatstatus',
            field=models.CharField(choices=[('3', '使用中'), ('1', '空闲'), ('4', '暂离'), ('2', '已预约')], default='1', max_length=5),
        ),
    ]
