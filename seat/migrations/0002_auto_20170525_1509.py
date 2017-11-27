# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrecord',
            name='orderstatus',
            field=models.CharField(max_length=1, default='1', choices=[('3', '过期'), ('2', '生效中'), ('1', '未在生效中')]),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatlevel',
            field=models.CharField(max_length=1, default='1', choices=[('3', '3楼'), ('4', '4楼'), ('5', '5楼'), ('2', '2楼'), ('1', '1楼')]),
        ),
    ]
