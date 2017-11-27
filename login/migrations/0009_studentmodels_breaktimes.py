# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20170518_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodels',
            name='breaktimes',
            field=models.IntegerField(default=0),
        ),
    ]
