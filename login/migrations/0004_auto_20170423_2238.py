# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20170416_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodels',
            name='academy',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentmodels',
            name='begin',
            field=models.CharField(max_length=8, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentmodels',
            name='break_times',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='studentmodels',
            name='condition',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='studentmodels',
            name='finish',
            field=models.CharField(max_length=8, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentmodels',
            name='floor',
            field=models.CharField(max_length=2, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentmodels',
            name='seat',
            field=models.CharField(max_length=6, blank=True, null=True),
        ),
    ]
