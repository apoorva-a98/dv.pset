x=input("enter a number")
#print(len(x))
Y=x.split('.')
#print(y)

def sqr(a,b):
    S=int(a)**int(b)
    return S

def base_conversion2(y):
    sum=0
    power=len(y[0])
    for i in y[0]:
        #print(i,power)
        sum=sum+(int(i)*sqr(2,power))
        power=power-1

    power=-1
    for j in y[1]:
        #print(i,power)
        sum=sum+(int(j)*sqr(2,power))
        power=power-1

    return sum

print(base_conversion2(Y))
