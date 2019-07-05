# -*- coding: utf-8 -*-
"""
Created on Mon July 1 15:00:40 2019

@author: Sjoerd Gn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import csv


#%%

data = pd.read_csv("appdata.txt",  skip_blank_lines=True, delimiter = " ## ") #delimiter = " - ",
                   
#%%


#%%
for line in data["date - message"]:
    nline = line.split(" - ")
    try:
        nline = nline[1].split(":")
        print(nline[0])
    except: 
        print("No data")
                   
                   #%%
print(data.iloc[8701])

#%%

file = open("appdata.txt", "rb")
data = csv.reader(file, delimiter = "-")    
for row in data:
    print(row)
file.close()