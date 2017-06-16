# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=30, blank=False)
	logo = models.ImageField()
	wikipedia = models.CharField(max_length=300, blank=True)
	def __str__(self):
		return self.name

	def getWikiName(self):
		if not self.wikipedia:
			return None

		last_index = self.wikipedia.rfind("/")
		return self.wikipedia[last_index+1:]

	def getActualStock(self):
		try:
			return self.stocks.latest(field_name="date")
		except CompanyStockValue.DoesNotExist:
			return None

class CompanyStockValue(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="stocks")
	value = models.FloatField()
	date = models.DateTimeField(auto_now_add=True)
	previous = models.OneToOneField('self', blank=True, null=True)
	def getIncrement(self):
		return self.value - self.previous.value
	def getPercentIncrement(self):
		if self.previous:
			return (self.getIncrement() * 100) / self.previous.value
		return 0
	def __str__(self):
		date_str = self.date.strftime('%d/%m/%Y %H:%M')
		return "%s - %.2f at %s" %(self.company.name, self.value, date_str)

class Person(models.Model):
        first_name = models.CharField(max_length=30, blank=False)
        last_name = models.CharField(max_length=30, blank=False)
        mail = models.CharField(max_length=40, blank=False)
        companies = models.ManyToManyField(Company, related_name="persons")
        def __str__(self):
                return "%s %s" %(self.first_name, self.last_name)
