# A tuple is sequence of immutable python object

tup1 = ('physics','chemistry',1997,2000);
tup2 = ('operating system',2,3,4,5);
tup3 = "a","b","c","d";

# empty tuple
emptup1 = ();
# to write a tuple you must include comma(,) at last. if one value then it is more important for tuple

# tup = (50,);
# print(tup)

# Accessing values in tuples
print("tup[0]:",tup1[1])
print("tup2[1:5]",tup2[0])

# updating tuple
tup3    =   tup1+tup2
print("this is updating tuple",tup3)
# delete tuple
del tup3;
print(tup3)
# error becos there are no tuple are exist
