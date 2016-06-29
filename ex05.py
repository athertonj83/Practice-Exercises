#ex05

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]

for x in a:
    for y in b:
        if y==x and y not in c:
            c.append(y)
print("This is where a and b have the same items:",c)




# randomly generate lists
d=[]
e=[]
f=[]

for i in range(15):
    d.append(random.randrange(0,20))
    e.append(random.randrange(0,50))
print(d)
print(e)

for x in d:
    for y in e:
        if y==x and y not in f:
            f.append(y)
f.sort()
print("This is where d and e have the same items:",f)
