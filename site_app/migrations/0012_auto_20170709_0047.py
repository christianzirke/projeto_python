# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-09 03:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0011_auto_20170704_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='stock',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companynews',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 9, 0, 47, 18, 705731)),
        ),
        migrations.AlterField(
            model_name='companystockvalue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 9, 0, 47, 18, 705220)),
        ),
    ]
