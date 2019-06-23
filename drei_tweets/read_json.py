# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 22:34:33 2019

@author: Sjoerd Gn
"""
import json
from pprint import *

file = "output/tweets.json"

tweets = []

for line in open(file, 'r'):
    tweets.append(json.loads(line))

    
for i in range(len(tweets)):
    print(tweets[i]['coordinates'])

#pprint(tweets[0])