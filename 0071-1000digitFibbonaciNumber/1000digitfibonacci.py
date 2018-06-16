def FibonacciNumbers():
    L=[1,1]
    number=0
    divisor=10**1000
    while(number//10**1000<1):
        number=L[0]+L[1]
        L[0]=L[1]
        L[1]=number
    print(number)
    print("the number of digits",len(str(number)))
FibonacciNumbers()
