# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0012_auto_20171107_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='polling',
            options={'ordering': ['-status', 'trigger_time']},
        ),
        migrations.RenameField(
            model_name='polling',
            old_name='begin_time',
            new_name='trigger_time',
        ),
        migrations.RemoveField(
            model_name='polling',
            name='end_time',
        ),
        migrations.AddField(
            model_name='polling',
            name='seat_id',
            field=models.CharField(default='0000', max_length=5),
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='orderstatus',
            field=models.CharField(default='1', choices=[('2', '生效中'), ('4', '过渡期'), ('1', '未在生效中'), ('3', '过期')], max_length=5),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatlevel',
            field=models.CharField(default='1', choices=[('2', '2楼'), ('4', '4楼'), ('3', '3楼'), ('5', '5楼'), ('1', '1楼')], max_length=1),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatstatus',
            field=models.CharField(default='1', choices=[('1', '空闲'), ('2', '已预约'), ('3', '使用中'), ('4', '暂离')], max_length=5),
        ),
    ]
