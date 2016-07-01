#ex12

import random

#first and last of the string
a = [5, 10, 15, 20, 25]
b=random.sample(range(0,50),12)


def firstlast(list):
    print("Taking the first and last entries of this list:",list)
    print("The first:", list[0])
    print("The last:", list[-1])

firstlast(a)
firstlast(b)
