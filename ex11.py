#ex11 - prime function

def primeornot(i):
    rangei=range(2,i)
    divisors=[]

    for x in rangei:
        if i%x==0:
            divisors.append(x)

    if divisors!=[]:
        print(i,"is not a prime, as it divides into",divisors)
    else:
        print(i,"is a prime")

i=int(input("Please give me a number:"))
primeornot(i)
