# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0003_auto_20170602_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrecord',
            name='orderstatus',
            field=models.CharField(max_length=1, default='1', choices=[('3', '过期'), ('1', '未在生效中'), ('2', '生效中')]),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatlevel',
            field=models.CharField(max_length=1, default='1', choices=[('3', '3楼'), ('1', '1楼'), ('5', '5楼'), ('2', '2楼'), ('4', '4楼')]),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatstatus',
            field=models.CharField(max_length=1, default='1', choices=[('1', '空闲'), ('4', '暂离'), ('2', '已预约'), ('3', '使用中')]),
        ),
    ]
