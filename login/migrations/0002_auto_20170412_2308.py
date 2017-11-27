# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodels',
            name='begin',
            field=models.CharField(max_length=8, default=''),
        ),
        migrations.AddField(
            model_name='studentmodels',
            name='break_time',
            field=models.CharField(max_length=5, default=''),
        ),
        migrations.AddField(
            model_name='studentmodels',
            name='condition',
            field=models.BooleanField(default=''),
        ),
        migrations.AddField(
            model_name='studentmodels',
            name='finish',
            field=models.CharField(max_length=8, default=''),
        ),
        migrations.AddField(
            model_name='studentmodels',
            name='floor',
            field=models.CharField(max_length=2, default=''),
        ),
        migrations.AddField(
            model_name='studentmodels',
            name='seat',
            field=models.CharField(max_length=6, default=''),
        ),
    ]
