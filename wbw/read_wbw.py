# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:00:40 2019

# to do: 
- winnaar per maand
- relateren aan weer
- overall winnaar
- grootste uitgaven
- persoon meest gepaald op bepaalde woorden

@author: Sjoerd Gn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from pandas.plotting import table 
#%%

#%%

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
#%%    
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
#plt.savefig("cumulative_spending.png", dpi = 300)


#%%

# to what did we spent everything
spendings = ['bier', 'pils', 'kan', 'krat', 'munt', 'bonnen', 'langs de lijn', 'dixo', 'lunch', 'pizza', 'afmelden']

# for plotting
spend_names = ['bier', 'pils', 'kannen', 'kratten', 'munten',  'bonnen', 'langs de lijn', 'Dopie dixo', 'lunch', 'pizza', 'te laat afmelden',  'overig']

spent_goal = dict.fromkeys(spendings+['overig'], 0)


fig = plt.figure(figsize = (12,12))
for i in range(len(data['Amount'])):
    
    # Overig?
    to_goal = False
    
    for name_goal in spendings:
        if name_goal in data['Description'][i]:
            spent_goal[name_goal] += data['Amount'][i]
            to_goal = True
            
    if not to_goal:
        spent_goal['overig'] += data['Amount'][i]

ax = fig.add_subplot(1, 1, 1)    
plt.bar(range(len(spent_goal)), spent_goal.values())


major_ticks = np.arange(0, 6000, 1000)
minor_ticks = np.arange(0, 6000, 200)

ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

plt.grid(which = 'major', axis = 'y', linestyle = '-')
plt.grid(which = 'minor', axis = 'y', linestyle = ':')

plt.xticks(range(len(spent_goal)), spend_names, rotation = 33)
plt.xlabel("Waar hebben die mooie jongens dat aan uitgegeven?")
plt.ylabel("Keiharde euro's")
plt.title('Waar is dat geld dan precies heen gegaan?')

plt.savefig('direction_spending.png', dpi = 200)

#%%
print(data.iloc[29])

exp_data = data.sort_values(by=['Amount'], ascending = False)
exp_data = exp_data.reset_index()
plot_exp_data = exp_data[[ 'Amount', 'Who', 'Description', 'Participants']].iloc[0:33]

plot_exp_data.to_csv('highest_expenses.csv')

#%%

