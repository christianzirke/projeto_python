# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404 

import wikipedia

from .models import Company

# Create your views here.
def company_details(request, company_id):
	company = get_object_or_404(Company, pk=company_id)
	wiki_name = company.getWikiName()
	wiki_description = None
	wiki_url = None
	if wiki_name:
		wiki = wikipedia.page(company.getWikiName(), auto_suggest=True)
		content = wiki.content
		wiki_description = content[:content.find(".")+1]
		wiki_url = company.wikipedia
	print wiki_url
	return render(request, 'site_app/company_details.html', {"company": company, "wiki_url": wiki_url, "wiki_description": wiki_description})
