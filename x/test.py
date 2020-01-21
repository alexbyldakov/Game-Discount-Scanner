# -*- coding: utf-8 -*-
import re

f = open('src.html','r')
html=f.read()
f.close()
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
    