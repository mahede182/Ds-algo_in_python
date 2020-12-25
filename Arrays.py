# Basic operation
# Traverse, Insertion, Deletion, Search, Update

from array import *
# arrayName = array(typecodes, [Initializers])

# b=>signed integer size 1 byte/td
# B=>unsigned integer size 1 byte
# c=>char size 1byte
# i=>signed integer 2 bytes
# I=>unsigned integer 2 bytes
# f=>floating point 4 bytes
# d=>floating point 8 bytes

array1 = array('i',[10,20,30,40,50])

for x in array1:
    print(x)
    # accessing Array Element

print("This is index [0] element",array1[0])
print("this is index [1] element",array1[4])
 # insertion operation
array1.insert(3,60)
for x in array1:
    print(x)
array1.remove(20)
print("Remove 20 in the element of array1")
for x in array1:
    print(x)
# search operation
print("the index of 50 in the list",array1.index(50))
# update operation
array1[2] = 80
for x in array1:
    print(x)