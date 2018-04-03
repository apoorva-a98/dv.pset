def EvenFibonacciNumbers():
    L=[]
    L.append(1)
    L.append(1)
    number=0
    i=1
    sum=0
    while(number<4000001):
        number=L[i]+L[i-1]
        L.append(number)
        i=i+1

        if(number%2==0):
            sum=sum+number

    for i in range(len(L)-1,-1,-1):
        if(L[i]>4000000):
            L.pop(i)

    return L,"the sum is "+str(sum)

print(EvenFibonacciNumbers())
