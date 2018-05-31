def primeFactor(n):
    i=2
    L=[]
    while i*i <= n:
        if n%i!=0:
            i= i+1
        else:
            n=n//i
            L.append(i)
    if n>1:
        L.append(n)
    print (L)
    print ('largest prime factor:',L[-1])
primeFactor(600851475143)
