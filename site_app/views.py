# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as DjangoUser

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, get_object_or_404

from django.template import loader
from django.http import Http404, HttpResponseRedirect

from .models import Company, User
from .forms import UserRegistrationForm

import urllib

@login_required
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

@login_required
def dashboard(request):
	user = request.user.site_user
	companies = Company.objects.exclude(pk__in=user.companies.all())
	return render(request, 'site_app/dashboard.html', {"user": request.user.site_user, "companies": companies})

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			email =  userObj['email']
			password = userObj['password']
			if not (DjangoUser.objects.filter(username=username).exists() or DjangoUser.objects.filter(email=email).exists()):
				dj_user = DjangoUser.objects.create_user(username, email, password)
				User.objects.create(django_user=dj_user)
				user = authenticate(username = username, password = password)
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				raise forms.ValidationError('Email already registered')

	else:
		form = UserRegistrationForm()
	return render(request, 'registration/register.html', {'form' : form})

@csrf_exempt
def include_company(request):
	data = request.POST
	print ""
	print data["name"]
	print data["logo"]
	print data["nasdaq"]
	print ""
	Company.objects.create(name=data["name"], nasdaq=data["nasdaq"], logo=data["logo"])

	return None

@login_required
def follow_company(request, company_id):
	request.user.site_user.companies.add(company_id)
	request.user.site_user.save()
	return HttpResponseRedirect('/')

@login_required
def unfollow_company(request, company_id):
	request.user.site_user.companies.remove(company_id)
	request.user.site_user.save()
	return HttpResponseRedirect('/')
