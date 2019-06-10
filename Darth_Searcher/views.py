# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import swapi

def index(request):
	pjs = swapi.get_all("people")
	return render(request, "index.html", {'pjs': pjs.items})
	#pjss = swapi.get_person(5)
	#pjs = [pjss]
	#return render(request, "index.html", {'pjs': pjs})