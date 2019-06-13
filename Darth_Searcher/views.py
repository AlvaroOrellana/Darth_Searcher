# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import swapi

def index(request):
	#pjs = swapi.get_all("people")
	#return render(request, "index.html", {'pjs': pjs.items})
	pjss = swapi.get_person(5)
	pjs = [pjss]
	pjs.append(swapi.get_person(1))
	try:
		request.session['visited']
		print "existe"
	except:
		request.session['visited'] = {}
		print "no existe"
	return render(request, "index.html", {'pjs': pjs, 'visited': request.session['visited']})

def film_compare(request):
	film_search = request.POST.get('film_search',False)
	# request.session['visited'] = {}
	if not film_search:
		return redirect('Error')
	else:
		films, result = swapi.get_all("films").order_by("release_date"), []
		for film in films:
			if film_search.upper() in film.title.upper():
				result.append(film)
		return render(request, "detail.html", {'film_search': film_search, 'films': result})

def film_detail(request, ide):
	films = swapi.get_all("films")
	for film in films.items:
		if int(ide) == film.episode_id:
			request.session['visited'][film.title] = request.build_absolute_uri()
			print request.session['visited']
			return render(request, "film.html", {'f': film})

def error(request):
	return render(request, "error.html")