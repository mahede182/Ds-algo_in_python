# map also called chain map. a structure manage multiple dictionaries as one unit
# elemenating any duplicate keys
# best uses search through multiple dictionaries at a time
# creating chainmap

import collections
dict1   =   {'day1':'mon','day2': 'tue'}
dict2   =   {'day3':'wed','day1': 'thurs'}

res = collections.ChainMap(dict1,dict2)

# creating single dictionary
print(res.maps,'\n')
print('keys = {}'.format(list(res.keys())))
print('values = {}'.format(list(res.values())))
print('elements')
# print('keys = {}'.format(list(res.keys())))
for keys, val in res.items():
    print('{} = {}'.format(keys,val))
print()

# find specific value in the result
print('day3 in res: {}'.format('day1' in res))