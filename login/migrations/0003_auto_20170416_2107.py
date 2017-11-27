# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20170412_2308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodels',
            old_name='break_time',
            new_name='break_times',
        ),
    ]
