# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('apt_num', models.CharField(max_length=200)),
                ('vacant', models.NullBooleanField()),
                ('number_of_rooms', models.IntegerField()),
                ('property', models.ForeignKey(to='properties.Property')),
            ],
        ),
    ]
