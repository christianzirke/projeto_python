# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 15:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0006_auto_20170703_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companynews',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 3, 12, 25, 52, 322807)),
        ),
        migrations.AlterField(
            model_name='companystockvalue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 3, 12, 25, 52, 322006)),
        ),
    ]
