# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0006_auto_20170604_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='auto_token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_time', models.CharField(max_length=14)),
                ('end_time', models.CharField(max_length=14)),
                ('token_status', models.CharField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='orderid',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='orderstatus',
            field=models.CharField(default='1', choices=[('3', '过期'), ('4', '过渡期'), ('1', '未在生效中'), ('2', '生效中')], max_length=5),
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='timelong',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatid',
            field=models.CharField(default='0000', max_length=5),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatlevel',
            field=models.CharField(default='1', choices=[('3', '3楼'), ('1', '1楼'), ('4', '4楼'), ('2', '2楼'), ('5', '5楼')], max_length=1),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatstatus',
            field=models.CharField(default='1', choices=[('3', '使用中'), ('4', '暂离'), ('2', '已预约'), ('1', '空闲')], max_length=5),
        ),
    ]
