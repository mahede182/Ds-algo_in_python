# in math set:: collection of items not any particular order.
#set operation: union,intersection,difference and complement
# creating a set
days = set(["Mon","Tues","Wed","thu","Fri","Sat","Sun"])
months = {"jan","Feb","Mar"}
dates = {21,22,17}
print(days)
print(months)
print(dates)
set(['Wed', 'Sun', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat'])
set(['Jan', 'Mar', 'Feb'])
set([17, 21, 22])
# for d in days
#     print(d)
# union set
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)
# intersection
intersactionDays = DaysA & DaysB
print(intersactionDays)
# difference
diffDays = DaysA - DaysB
print(diffDays)
# compare days
subsetAB = DaysA <= DaysB
print(subsetAB)
# superset
superSet = DaysB >= DaysB
print(subsetAB)