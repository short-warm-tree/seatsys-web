# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20170518_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodels',
            name='mm',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='studentmodels',
            name='stuid',
            field=models.CharField(max_length=13),
        ),
    ]
