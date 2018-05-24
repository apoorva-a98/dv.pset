def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
x=str(factorial(100))

def cal_sum(y):
    i=0
    sum=0
    while i<len(y):
        sum=sum+(int(y[i]))
        i=i+1
    return sum

print("factorial is: "+str(x))
#print(len(x))
print("sum is: "+str(cal_sum(x)))
