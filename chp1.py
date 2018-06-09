# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import seaborn as sns
import matplot as mtplt

''' string manipulation ..'''

lat = '43.32 N'
lon = '73.528 W'
s= "the location of this restaurant is {latd} in latitude, and {lond} in longitude"
s.format(latd=lat,lond=lon)

len(("Happy " + "Bday ")*3)
print(("Happy " + "Bday ")*3)

''' boolean '''

print('N' in lat)
if 'N' in lat:
    print('Restaurant is in the northern Hemispher')
else:
    print('Restaurant may not be in the northern Hemispher')
x = 5
if x > 1 and x < 10:
    print('variable x is a single digit above 1')
if x < 0 or 'N' in lat:
    print('variabke x is positive and restaurant is in Northern Hemi')
sister =15
brother= 13
if brother > sister:
    print('brother is older than sister')
elif brother == sister:
    print('brother and sister are twins')
else:
    print('sister is older than brother')

''' Lists '''

my_fav_states = ['California', 'Florida', 'Nevada', 'Texas', 'Virginia', 'North_Carolina',
                 'South_Carolina', 'Georgia']
my_fav_states.append('New_Mexico')
print(my_fav_states)
if 'N' in my_fav_states[2]:
    print(my_fav_states)
my_fav_states.reverse()
print(my_fav_states)
my_fav_states.append('Florida')
if 'Florida' in my_fav_states:
    print('Florida is included in the list #' + str(my_fav_states.count('Florida')) + ' times')

        
    
    
    

