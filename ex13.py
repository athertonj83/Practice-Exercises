#ex13 - Fibonacci numbers

def fib(n):
    fibr=[0,1]

    if n>2:
        for x in range(3,n+1):
            fibr.append(fibr[x-2]+fibr[x-3])
    print(fibr)

n=int(input("Please enter the number of fibonacci numbers you'd like: "))
fib(n)
