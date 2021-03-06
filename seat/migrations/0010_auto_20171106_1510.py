# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0009_auto_20171106_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='polling',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('begin_time', models.CharField(max_length=14)),
                ('end_time', models.CharField(max_length=14)),
                ('owner_id', models.TextField(default=0)),
                ('source_id', models.TextField(default=0)),
                ('status', models.CharField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='orderstatus',
            field=models.CharField(max_length=5, default='1', choices=[('4', '过渡期'), ('3', '过期'), ('1', '未在生效中'), ('2', '生效中')]),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatlevel',
            field=models.CharField(max_length=1, default='1', choices=[('3', '3楼'), ('1', '1楼'), ('5', '5楼'), ('2', '2楼'), ('4', '4楼')]),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seatstatus',
            field=models.CharField(max_length=5, default='1', choices=[('4', '暂离'), ('2', '已预约'), ('3', '使用中'), ('1', '空闲')]),
        ),
    ]
