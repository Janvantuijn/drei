# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:00:40 2019

@author: Sjoerd Gn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data.txt", sep = '\t')
data['Amount']=data['Amount'].replace('\u20AC','',regex=True).astype(float)

#print(data['Participants'])

members_data = pd.read_csv('members.txt', sep = '#')


members = [members_data['names'][i] for i in np.arange(0, len(members_data['names']), 2)]


result = {}
for name in members:
    result[name] = pd.DataFrame(columns = ['date', 'cost', 'sum_cost'])


    
for i in range(len(data)):
    gepaald = data['Participants'][i].split(', ')
    cost = data['Amount'][i]/len(gepaald)
    date = data['Date'][i]
    
    for name in gepaald:
       
        result[name] = result[name].append({'date': date, 
              'cost': cost, 'sum_cost': cost}, ignore_index = True)
    
plt.figure(figsize = (12,12))
for name in members:
    result[name]['date'] = pd.to_datetime(result[name]['date'], format='%d-%m-%Y')
    result[name] = result[name].sort_values(by = 'date')
    result[name] = result[name].reset_index(drop=True)
    for i in range(1, len(result[name]['cost'])):
        result[name]['sum_cost'][i] = sum(result[name]['cost'][:i+1])
    plt.plot(result[name]['date'], result[name]['sum_cost'], label = name)
 
plt.xlabel("Datum")
plt.ylabel("Cumulatief gespendeerd")
plt.title("Wanneer hebben die mooie jongens al dat geld gespendeerd?")
plt.legend()
plt.savefig("cumulative_spending.png", dpi = 300)
