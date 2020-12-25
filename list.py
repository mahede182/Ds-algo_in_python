list1 = ['physics','chemistry',1997,2000]
list2 = [1,2,3,4,5,6,7]
#        0 1 2 3 4 5 6
print("list1[0]",list1[0])
print("list[1:5]",list2[1:5])
# updating list
list = ['physics','chemistry',1997,2000]
print("Value available at index 2:")
print(list[2])
list[2] = 2001
print("New value available at index 2:")
print(list[2])
# Delete list elements
print(list1)
del list1[2]
print("After deleting value at index 2 :")
print(list1)
### basic list operation

# python exp: len([1,2,3])   [1,2,3]+[4,5,6]   ["hi"]*2       3 in [1,2,3]
# Result            3        [1,2,3,4,5,6]    ['hi']['hi']    True
# Description       Length   concatanation    itaration       Membership