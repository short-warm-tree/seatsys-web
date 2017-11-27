# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0008_auto_20171105_0649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auto_token',
            options={'ordering': ['begin_time']},
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='orderstatus',
            field=models.CharField(choices=[('1', '未在生效中'), ('3', '过期'), ('4', '过渡期'), ('2', '生效中')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatlevel',
            field=models.CharField(choices=[('2', '2楼'), ('4', '4楼'), ('1', '1楼'), ('3', '3楼'), ('5', '5楼')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatstatus',
            field=models.CharField(choices=[('2', '已预约'), ('4', '暂离'), ('1', '空闲'), ('3', '使用中')], default='1', max_length=5),
        ),
    ]
