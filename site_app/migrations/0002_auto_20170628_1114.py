# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 14:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companystockvalue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 11, 14, 33, 348551)),
        ),
    ]