#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A quick & dirty script to convert the OctoberCMS blog posts from a CSV export

Needs to download the images from the live page
"""

import os
import requests
import shutil
from bs4 import BeautifulSoup
import subprocess
import re

def create_post(row):
    # ID,Title,Content,Excerpt,Slug,Categories,"Created date","Updated date","Published date"
    title = row[1]
    content = row[2]
    excerpt = row[3]
    slug = row[4]
    categories = [_ for _ in row[5].split('|') if _ not in ['German', 'English', 'Français', 'Italian', 'Russian']]
    categories = ', '.join(categories + ['old blog'])
    published = row[8].split(' ')[0].replace('"', "'")

    # create directory for post
    try:
        shutil.rmtree(slug)
    except:
        pass
    os.mkdir(slug)
    
    
    # create header
    header = """---
title: '{}'
date: '{}'
continue_link: true
taxonomy:
    category: blog
    tag: [{}]
---
    """.format(title, published, categories)
    
    # download images
    imgs = re.findall(r"/storage/app/\S+?\)", content)
    print(imgs)
    for i in imgs:
        i = i[:-1]
        subprocess.run(['wget', 'https://project.yunity.org'+i], cwd=slug)
        content = content.replace(i, i.split('/')[-1])
    
    # write header and content into item.md
    with open(os.path.join(slug, 'item.md'), 'w+') as f:
        f.write(header)
        f.write("\n\n")
        f.write(excerpt)
        f.write("\n\n===\n\n")
        f.write(content)
        
    
    # copy featured image
    r = requests.get('https://project.yunity.org/blog/post/{}'.format(slug))
    soup = BeautifulSoup(r.text, 'html.parser')
    img = soup.find('div', class_='featured-images').find('img')
    subprocess.run(['wget', img.attrs['src']], cwd=slug)

import csv
with open('posts.csv') as f:
    c = csv.reader(f)
    for row in c:
        create_post(row)
        