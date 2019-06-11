# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import swapi

def index(request):
	#pjs = swapi.get_all("people")
	#return render(request, "index.html", {'pjs': pjs.items})
	pjss = swapi.get_person(5)
	pjs = [pjss]
	pjs.append(swapi.get_person(1))
	return render(request, "index.html", {'pjs': pjs})

def film_compare(request):
	film_search = request.POST.get('film_search',False)
	if not film_search:
		return render(request, "error.html")
	else:
		films, result = swapi.get_all("films").order_by("release_date"), []
		for film in films:
			if film_search.upper() in film.title.upper():
				result.append(film)
		return render(request, "detail.html", {'film_search': film_search, 'films': result})