# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_apartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='history',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
