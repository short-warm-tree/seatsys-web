# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20170518_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodels',
            name='mm',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentmodels',
            name='stuid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentmodels',
            name='value',
            field=models.IntegerField(default=100),
        ),
    ]
