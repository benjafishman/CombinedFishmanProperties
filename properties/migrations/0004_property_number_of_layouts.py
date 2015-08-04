# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_property_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='number_of_layouts',
            field=models.IntegerField(default=0),
        ),
    ]
