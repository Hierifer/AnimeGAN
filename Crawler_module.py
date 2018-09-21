#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 15:41:51 2018

@author: zijiachen & Teng Hu
"""

import requests
from bs4 import BeautifulSoup
import os 
import sys
import traceback 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traceback

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

def img_downloader(url, url_filter='', path='imgs'):
    if os.path.exists(path) is False:
        os.makedirs(path)
    
    c=0
    t=time.time()
    # windows only
    #browser = webdriver.Chrome('/home/hierifer/Desktop/AnimeGAN/chromedriver.exe')
    browser = webdriver.Chrome('/home/hierifer/Desktop/AnimeGAN/chromedriver')
    try:
        
        browser.get(url)
        html = browser.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        time.sleep(1)
        html.send_keys(Keys.END)
        time.sleep(1)
        html.send_keys(Keys.END)
        imgs = browser.find_elements_by_tag_name('img')
    
        print(html.text)
        for i in range(len(imgs)):
            img_url = imgs[i].get_attribute("src")
            
            if url_filter in img_url:
                filename = os.path.join('imgs', img_url.split('/')[-1])
                download(img_url, filename)
            c+=1    
                
        browser.quit()
        print("Visited: " + url + " Downloaded Images: " +str(c))
        print('time:%f'%(time.time()-t))
    except:
        browser.quit()
        print("Some Errors Raised on img_downloader:", sys.exc_info()[0])

def pinterest_img_downloader(url='', keyword='', url_filter='', path='imgs'):
    if(keyword !=''):
        keyword.lower()
        keyword.replace(' ','%20')
        url = "https://www.pinterest.com/search/pins/?q="+keyword
    if os.path.exists(path) is False:
        os.makedirs(path)
    
    c=0
    t=time.time()
    # windows only
    #browser = webdriver.Chrome('/home/hierifer/Desktop/AnimeGAN/chromedriver.exe')
    browser = webdriver.Chrome('/home/hierifer/Desktop/AnimeGAN/chromedriver')
    try:
        if(url !=''):
            browser.get(url)
        last = 0
        cur = 1
        p = 0
        while(cur > last):   
            last = cur
            html = browser.find_element_by_tag_name('html')
            cur = len(html.text)
            html.send_keys(Keys.END)
            time.sleep(3)
            p+=1
        
        
        imgs = browser.find_elements_by_tag_name('img')
        
        for i in range(len(imgs)):
            img_url = imgs[i].get_attribute("src")
            
            if url_filter in img_url:
                filename = os.path.join('imgs', img_url.split('/')[-1])
                download(img_url, filename)
            c+=1    
              
        print("Visited: " + url + " Pages Scrolled:" + str(p) +" Downloaded Images: " +str(c))
        print('time:%f'%(time.time()-t))
        browser.quit()
    except:
        browser.quit()
        print("Some Errors Raised on img_downloader: ",sys.exc_info()[0])
        traceback.print_exc()
   
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

pinterest_img_downloader(keyword="touhou", url_filter="pinimg")

