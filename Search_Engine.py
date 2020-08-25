# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 03:10:56 2020

@author: lenovo
"""

import sqlite3
from bs4 import BeautifulSoup
import re

conn = sqlite3.connect('spider_wiki.sqlite')
cur = conn.cursor()

searched = str(input("Search in Wikipedia: "))
cur.execute("SELECT url, html FROM Pages WHERE html LIKE '%"+searched+"%' ORDER BY new_rank")

urllist = []
desclist = []
i = 0
for url, html in cur:
    if url is None: 
        print("No search results found!")
        break
    else:
        urllist.append(url)
    
        code = str(html)
        soup = BeautifulSoup(code, "html.parser")
        paras = soup('p')
    
        for para in paras:
            p = re.findall('<p>(.*)</p>', str(para))
            desclist.append(p[0])
    
    
        i += 1
        if i == 15:
            break
    
print(urllist)
print(desclist)