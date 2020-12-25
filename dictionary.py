# in dictionary each key separated from its value by a colon(:) and {}
# Acessing values in dictionary
dict = {'name': 'mahede hasan','age':22,'class':'first'}
print("dictionary ['name']",dict['name'])
print("age",dict['age'])
# updating dictionary

dict['age'] = 23
print(dict)
 # remove entry
del dict['name']
print(dict)
# remove all entrys
dict.clear()
print("the dictionary are cleared",dict)