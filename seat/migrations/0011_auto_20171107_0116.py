# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0010_auto_20171106_1510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auto_token',
            options={'ordering': ['-token_status', 'begin_time']},
        ),
        migrations.AlterModelOptions(
            name='polling',
            options={'ordering': ['-status', 'end_time']},
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='orderstatus',
            field=models.CharField(max_length=5, default='1', choices=[('4', '过渡期'), ('2', '生效中'), ('1', '未在生效中'), ('3', '过期')]),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatlevel',
            field=models.CharField(max_length=1, default='1', choices=[('5', '5楼'), ('4', '4楼'), ('3', '3楼'), ('2', '2楼'), ('1', '1楼')]),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatstatus',
            field=models.CharField(max_length=5, default='1', choices=[('3', '使用中'), ('1', '空闲'), ('2', '已预约'), ('4', '暂离')]),
        ),
    ]
