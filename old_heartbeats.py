#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 17:07:53 2017

@author: tic
"""


#%% get urls of posts
url = "https://yunity.atlassian.net/wiki/pages/viewrecentblogposts.action?key=YUN"
from bs4 import BeautifulSoup
import requests

urls = []

while url:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for post in soup.find_all('div', class_='blog-post-listing'):
        link = post.find('a', class_='blogHeading')
        urls.append(link.get('href'))
        print(link)
        
    url = 'https://yunity.atlassian.net' + soup.find('a', class_='blogmonthnavigation').get('href')
    # repeats endlessly for now
print(urls)

#%% get posts
import os
import re

urls = list(set(urls))
os.mkdir('old_heartbeats')
for u in urls:
    r = requests.get('https://yunity.atlassian.net' + u)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find(id='title-text').a.get_text()
    print(title)
    date = re.search(r'\d{4}-\d{2}-\d{2}', title).group()
    html = soup.find(id='main-content').div.prettify()
    
    os.mkdir(os.path.join('old_heartbeats', date))
    with open(os.path.join('old_heartbeats', date, 'source.html'), 'w+') as f:
        f.write('<h1>{}</h1>'.format(title))
        f.write(html)
        
        
#%%
import os
from bs4 import BeautifulSoup

#os.chdir('user/pages/01.heartbeat')
for d in os.listdir():
    if d == 'blog.md':
        continue
    if 'item.md' in os.listdir(d):
        continue
    
    print(d)
    with open(os.path.join(d, 'source.html')) as f:
        soup = BeautifulSoup(f, 'html.parser')
        header = """---
title: "{}"
date: "{}"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
published: false
---

""".format(soup.h1.extract(), d)

        for url in soup.find_all('a'):
            if not url['href'].startswith('http'):
                url['href'] = 'https://yunity.atlassian.net' + url['href']

        with open(os.path.join(d, 'item.md'), 'w+') as dest:
            dest.write(header)
            dest.write(soup.prettify())
            
