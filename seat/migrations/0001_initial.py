# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20170518_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderrecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('orderid', models.CharField(max_length=9, default='')),
                ('fromtime', models.TimeField(default='')),
                ('endtime', models.TimeField(default='')),
                ('orderstatus', models.CharField(max_length=1, default='1', choices=[('2', '生效中'), ('1', '未在生效中'), ('3', '过期')])),
            ],
        ),
        migrations.CreateModel(
            name='seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('seatid', models.CharField(max_length=4, default='0000')),
                ('seatlevel', models.CharField(max_length=1, default='1', choices=[('4', '4楼'), ('2', '2楼'), ('5', '5楼'), ('3', '3楼'), ('1', '1楼')])),
                ('seatstatus', models.CharField(max_length=1, default='1', choices=[('4', '暂离'), ('1', '空闲'), ('2', '已预约'), ('3', '使用中')])),
            ],
            options={
                'ordering': ['seatid'],
            },
        ),
        migrations.AddField(
            model_name='orderrecord',
            name='seat',
            field=models.ForeignKey(default='', to='seat.seat'),
        ),
        migrations.AddField(
            model_name='orderrecord',
            name='student',
            field=models.ForeignKey(default='', to='login.StudentModels'),
        ),
    ]
