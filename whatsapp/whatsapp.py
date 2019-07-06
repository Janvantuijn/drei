# -*- coding: utf-8 -*-
"""
Created on Mon July 1 15:00:40 2019

@author: Sjoerd Gn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import csv
import collections

#%%

data = pd.read_csv("appdata.txt",  skip_blank_lines=True, delimiter = " ## ") #delimiter = " - ",
        
#%%

countmessages = {}
#%%
count = 0
for line in data["date - message"]:
    count +=1
    if count > 0: #33948:    #sinds 
        nline = line.split(" - ")
        try:
            nline = nline[1].split(":")
            if nline[0] in countmessages:
                countmessages[nline[0]] += 1
            else:
                countmessages[nline[0]] = 1
        except: 
            pass
            #print("No data")
            
print(countmessages)
                   #%%

cm = {i:countmessages[i] for i in countmessages if countmessages[i] > 10} 
cm = sorted(cm.items(), key=lambda kv: kv[1], reverse=True)
cm = collections.OrderedDict(cm)

#%%

fig = plt.figure(figsize = (15,15))  
ax = fig.add_subplot(1, 1, 1)   

major_ticks = np.arange(0, 8000, 500)
minor_ticks = np.arange(0, 8000, 100)

ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)
plt.grid(which = 'major', axis = 'y', linestyle = '-')
plt.grid(which = 'minor', axis = 'y', linestyle = ':')   
     
plt.bar(cm.keys(), cm.values())
plt.xticks(rotation = 90)


plt.ylabel("Aantal whatsappjes")
plt.title("Hoevaak hebben die mooie jongens dan gewhatsappt sinds 26 augustus 2018?")
plt.savefig("Whatsappmesssent2.png", dpi = 200)

#%%

file = open("appdata.txt", "rb")
data = csv.reader(file, delimiter = "-")    
for row in data:
    print(row)
file.close()

#%%

print(sum(cm.values()))