# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20170423_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmodels',
            name='begin',
        ),
        migrations.RemoveField(
            model_name='studentmodels',
            name='break_times',
        ),
        migrations.RemoveField(
            model_name='studentmodels',
            name='finish',
        ),
        migrations.RemoveField(
            model_name='studentmodels',
            name='floor',
        ),
        migrations.RemoveField(
            model_name='studentmodels',
            name='seat',
        ),
        migrations.AddField(
            model_name='studentmodels',
            name='value',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='studentmodels',
            name='academy',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
