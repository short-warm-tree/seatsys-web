# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0002_auto_20170525_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderrecord',
            name='endtime',
        ),
        migrations.AddField(
            model_name='orderrecord',
            name='timelong',
            field=models.CharField(max_length=1, default=''),
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='orderstatus',
            field=models.CharField(max_length=1, default='1', choices=[('1', '未在生效中'), ('3', '过期'), ('2', '生效中')]),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatlevel',
            field=models.CharField(max_length=1, default='1', choices=[('4', '4楼'), ('5', '5楼'), ('3', '3楼'), ('2', '2楼'), ('1', '1楼')]),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatstatus',
            field=models.CharField(max_length=1, default='1', choices=[('3', '使用中'), ('2', '已预约'), ('4', '暂离'), ('1', '空闲')]),
        ),
    ]
