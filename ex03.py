# list exercise

def ex03():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    print("This is a:")
    for num in a:
        if num<5:
            print(num)


    #b) trying to populate a new list - works
    for num in a:
        if num<5:
            b.append(num)
    print("This is b:",b)


    #c) deleting those in the existing list - using filter & lambda
    c=list(filter(lambda num: num<5, c))
    print("This is c:",c)


if __name__=='__main__':
    ex03()
