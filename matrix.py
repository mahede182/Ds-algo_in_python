from numpy import *
# 1 week measure moring,midday,evening,midnight
a = array([['Mon', 18, 20, 22, 17],
           ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19],
           ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22],
           ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])

m = reshape(a, (7, 5))
print(m)
# print data for Wednesday

print("print data for Wednessday",m[2])
# print friday evening
print("friday evening",m[4][3])
# adding a row
m_r = append(m,[['Avg',12,15,13,11]],0)
print(m_r)
# adding a coulumn
m_c = insert(m,[4],[[1],[2],[3],[4],[5],[6],[7]],1)
print(m_c)
# delete a row matrics
m = delete(m,[2],0)
print('delete 3 no row',m)