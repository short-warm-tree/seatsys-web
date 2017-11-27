# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20170518_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodels',
            name='value',
            field=models.CharField(max_length=4, default='100'),
        ),
    ]
