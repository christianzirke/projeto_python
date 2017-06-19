# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404

from .models import Company, Person

import urllib

# Create your views here.
def company_details(request, company_id):
	company = get_object_or_404(Company, pk=company_id)
	wiki_url = company.wikipedia
	text = None
	# if wiki_url:
	# 	text = urllib.urlopen(wiki_url).read()
	# 	print text
	 # 	idx = text.find('<table class="infobox')
	# 	text = text[idx:]
	# 	text = text[:text.find('</table>') + 8]
	# 	print text
	return render(request, 'site_app/company_details.html', {"company": company, "wiki_url": wiki_url, "wiki_description": text})

def dashboard(request, user_id):
	user = get_object_or_404(Person, pk=user_id)
	return render(request, 'site_app/dashboard.html', {"user": user})
