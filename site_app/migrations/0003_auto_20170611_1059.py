# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0002_companystockvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companystockvalue',
            name='previous',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_app.CompanyStockValue'),
        ),
    ]
