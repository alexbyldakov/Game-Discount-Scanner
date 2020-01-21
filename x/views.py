# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from x.models import *
import re
import requests

def update(request):
	#a = "http://store.steampowered.com/search/?specials=1&os=win" 
	#a = "http://store.steampowered.com/search/?specials=1&os=win&sort_by=&sort_order=0&specials=1&os=win&page=2"
	#a = "http://store.steampowered.com/search/?specials=1&os=win&sort_by=&sort_order=0&specials=1&os=win&page=3"
	#a = "http://store.steampowered.com/search/?specials=1&os=win&sort_by=&sort_order=0&specials=1&os=win&page=4"
	#a = "http://store.steampowered.com/search/?specials=1&os=win&sort_by=&sort_order=0&specials=1&os=win&page=5"
	a = "http://store.steampowered.com/search/?specials=1&os=win&sort_by=&sort_order=0&specials=1&os=win&page=6"
	html = requests.get(a)
	html = html.text.encode('utf8')
	#f = open('x\\src.html','r')
	#html=f.read()
	#f.close()
	chunks = html.split('<div class="col search_capsule">')
	for chunk in chunks[1:]:
		r = re.findall('src="(.+?)" alt="Buy (.+?)"', chunk)
		src, name = r[0][0], r[0][1]
		name = name.replace('™','').replace('&amp;','&').replace('&trade;','')
		
		r = re.findall('<strike>(.+?) ', chunk)
		cost_original = float(r[0].replace(',','.'))
		r = re.findall('<br>(.+?) ', chunk)
		cost_discount = float(r[0].replace(',','.'))
		r = re.findall('<span>-(.+?)%</span>', chunk)
		discount = int(r[0])
		print name, cost_original, cost_discount, discount
		g,cr = Game.objects.get_or_create(name=name, price1=cost_original, price2=cost_discount, discount=discount, image=src)
		print g.id, cr
	return HttpResponse("ok")
	
def home(request):
	games = Game.objects.all().order_by('id')
	q = request.GET.get('q')
	if q:
		games = games.filter(name__icontains=q)
	ctx = {'games':games}
	return	render_to_response('home.html', context_instance=RequestContext(request, ctx))