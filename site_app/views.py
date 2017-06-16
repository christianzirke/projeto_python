# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404

import wptools

from .models import Company, Person

# Create your views here.
def company_details(request, company_id):
	company = get_object_or_404(Company, pk=company_id)
	wiki_name = company.getWikiName()
	wiki_description = None
	wiki_url = None
	if wiki_name:
		wiki = wptools.page(company.getWikiName(), auto_suggest=True).get_parse()
		content = wiki.infobox
		wiki_description = "Descricao teste pq caguei as outras coisas"
		#wiki_description = content[:content.find(".")+1]
		wiki_url = company.wikipedia
	print wiki_url
	return render(request, 'site_app/company_details.html', {"company": company, "wiki_url": wiki_url, "wiki_description": wiki_description})

def dashboard(request, user_id):
	user = get_object_or_404(Person, pk=user_id)
	print(user.companies)
	return render(request, 'site_app/dashboard.html', {"user": user})
