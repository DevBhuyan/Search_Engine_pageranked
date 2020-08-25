# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 02:35:20 2020

@author: lenovo
"""


import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.executescript('''
            DROP TABLE IF EXISTS Pages;
            DROP TABLE IF EXISTS Links;
            DROP TABLE IF EXISTS Webs''')
print("TABLES Pages, Links and Webs have been DROPPED")
            
conn.commit()
cur.close()