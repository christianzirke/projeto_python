# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=30, blank=False)
	logo = models.FileField()
	def __str__(self):
		return self.name

	def getActualShare(self):
		try:
			return self.shares.latest(field_name="date")
		except CompanyShareValue.DoesNotExist:
			return None

class Person(models.Model):
        first_name = models.CharField(max_length=30, blank=False)
        last_name = models.CharField(max_length=30, blank=False)
        mail = models.CharField(max_length=40, blank=False)
        companies = models.ManyToManyField(Company, related_name="persons")
        def __str__(self):
                return "%s %s" %(self.first_name, self.last_name)

class CompanyShareValue(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="shares")
	value = models.FloatField()
	date = models.DateTimeField()
	def __str__(self):
		date_str = self.date.strftime('%d/%m/%Y %H:%M')
		return "%s - %.2f at %s" %(self.company.name, self.value, date_str)
