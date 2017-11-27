# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0011_auto_20171107_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='polling',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='orderstatus',
            field=models.CharField(default='1', max_length=5, choices=[('4', '过渡期'), ('1', '未在生效中'), ('2', '生效中'), ('3', '过期')]),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatlevel',
            field=models.CharField(default='1', max_length=1, choices=[('1', '1楼'), ('4', '4楼'), ('3', '3楼'), ('2', '2楼'), ('5', '5楼')]),
        ),
    ]
