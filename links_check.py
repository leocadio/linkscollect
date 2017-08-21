# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:30:27 2017

@author: Leocadio
"""

# -*- coding: utf-8 -*-
"""
тестовая часть / знакомство с библиотекой
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup 

def internLinks(startPage):
    """
    на входе: адрес стартовой страницы
    на выходе: список всех внутренних ссылок сайта 
    """
    links_raw = []
    links2 = []
    links = []
    
    from urllib.request import urlopen
    from bs4 import BeautifulSoup 
    html = urlopen(startPage)
    bsObj = BeautifulSoup(html.read(), "html5lib")

#формируем начальный "сырой" список ссылок с заглавной страницы
#    links_raw = []
    for link in bsObj.find_all('a'):
        if link not in links_raw:
            if len(link)>0:
                links_raw.append(link.get('href'))
        print (link)    
#формируем "чистовой" список ссылок с заглавной страницы
 #   links2 = []
    for l in links_raw:
        if len(l)>5 and l[:4]!='http':
            links2.append(l) 
       
# прогоняем один цикл по всем внутренним ссылкам с главной страницы      
    for link in links2:
        html = urlopen(startPage + '/'+ link)
        bsObj = BeautifulSoup(html.read(), "html5lib")
        for lnk in bsObj.find_all('a'):
            if lnk not in links_raw:
                if len(lnk)>0:
                    links_raw.append(lnk.get('href'))
    
#формируем итоговый "чистовой" список
#    links = []
    for li in links_raw:
        if len(li)>5 and li[:4]!='http':
            links.append(startPage + li)
    return links

import re

def iherbLinks(startPage):
    intLinks = internLinks(startPage)
    for link in intLinks:
        html = urlopen(startPage + link)
        bsObj = BeautifulSoup(html.read(), "html5lib")
        for lnk in bsObj.find_all('a', {"href":re.compile("iherb\.com")}):
            if lnk not in links:
                links.append(lnk.get('href'))
        return links
                    