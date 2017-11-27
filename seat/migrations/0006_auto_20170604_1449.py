# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0005_auto_20170604_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seatlevel',
            field=models.CharField(default='1', choices=[('1', '1楼'), ('2', '2楼'), ('5', '5楼'), ('4', '4楼'), ('3', '3楼')], max_length=1),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatstatus',
            field=models.CharField(default='1', choices=[('1', '空闲'), ('2', '已预约'), ('4', '暂离'), ('3', '使用中')], max_length=1),
        ),
    ]
