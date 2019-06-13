# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import swapi

def index(request):
	try:
		request.session['visited']
	except:
		request.session['visited'] = {}
	""" BLOQUE TODOS LOS PERSONAJES """
	# pjss = swapi.get_all("people")
	# pjs = [pjss]
	""" FIN BLOQUE """
	""" BLOQUE DIEZ PRIMEROS PERSONAJES """
	pjs = []
	for i in range(1,11):
		pjs.append(swapi.get_person(i))
	""" FIN BLOQUE """
	return render(request, "index.html", {'pjs': pjs, 'visited': request.session['visited']})

def film_compare(request):
	film_search = request.POST.get('film_search',False)
	if not film_search or len(film_search) < 1:
		return redirect('Error')
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
			return render(request, "film.html", {'f': film})

def error(request):
	return render(request, "error.html")