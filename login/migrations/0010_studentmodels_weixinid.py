# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_studentmodels_breaktimes'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodels',
            name='weixinid',
            field=models.CharField(null=True, max_length=100),
        ),
    ]
