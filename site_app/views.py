# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404

from django.template import loader
from django.http import Http404

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
	return render(request, 'site_app/dashboard.html', {"user": request.user})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Email already registered')

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form' : form})

def logout(request):
	logout(request)
