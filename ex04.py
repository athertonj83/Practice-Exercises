#ex04

def ex04():
    while True:
        num=input("Please supply an integer:")

        if not num.isnumeric():
            continue
        else:
            break

    new_list=range(1,int(num)+1)
    y=[]

    for x in new_list:
        if int(num)%x==0:
            y.append(x)
    print("Here are the divisors for your supplied number:",y)

if __name__=='__main__':
    ex04()
