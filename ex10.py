#ex10

import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a=random.sample(range(50),10)
print("a:",a)
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b=random.sample(range(20),10)
print("b:",b)

c=[x for x in a if x in b]
print("Overlap:",c)

d=[]
for i in c:
    if i not in d:
        d.append(i)
print("Overlap with no duplicates:",d)
