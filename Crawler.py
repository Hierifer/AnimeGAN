#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 15:41:51 2018

@author: zijiachen
"""

import requests
from bs4 import BeautifulSoup
import os 
import traceback 
import time

def download(url,filename):
    try:
        r=requests.get(url)
        r.raise_for_status()
        with open(filename, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=65536):
                if chunk:
                    fd.write(chunk)
                    fd.flush()
            return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)

def img_downloader(url):
    t=time.time()
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all('img', class_="preview"):
        img_url = img['src']
        filename = os.path.join('imgs', img_url.split('/')[-1])
        download(img_url, filename)
    print("Visited: " + url)
    print('time:%f'%(time.time()-t))


#Main Downloader


'''
if os.path.exists('imgs') is False:
    os.makedirs('imgs')

start = 1
end = 2000
t=time.time()
for i in range(start, end + 1):
    url = 'https://yande.re/post?page=%d' % i
    print("Visited " + url)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all('img', class_="preview"):
        img_url = img['src']
        filename = os.path.join('imgs', img_url.split('/')[-1])
        download(img_url, filename)
    print('%d / %d' % (i, end))
    print('time:%f'%(time.time()-t))
'''



img_downloader("https://www.pinterest.com/pin/620089442420495027/")