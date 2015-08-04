# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_property_number_of_layouts'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image_file',
            field=models.CharField(max_length=200, default='none'),
        ),
    ]
