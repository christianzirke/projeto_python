# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Company, Person, CompanyStockValue

# Register your models here.
admin.site.register(Company)
admin.site.register(Person)
admin.site.register(CompanyStockValue)
