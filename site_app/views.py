# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404 

from .models import Company

# Create your views here.
def company_details(request, company_id):
	company = get_object_or_404(Company, pk=company_id)
	return render(request, 'site_app/index.html', {"company": company})
