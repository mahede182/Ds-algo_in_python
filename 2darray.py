from array import *
T = [[11,12,13],[15,6,2],[12,15,8,6]]
print(T[0])
print(T[1][1])
# value above different row
for r in T:
    for c in r:
        print(c, end=' ')
    print()