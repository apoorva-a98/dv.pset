n=int(input("enter the limit: "))

def all(x):
    sum=0
    for i in range(n+1):
        sum=sum+i
    return sum

def consec(x):
    sum=0
    for i in range(3,n+1,2):
        sum=sum+i
    return sum

def not_square(x):
    sum=0
    for i in range(1,n+1,1):
        sum=sum+i
        for j in range(2,i+1,1):
            test=i//j
            check=test*test
            if(check==i):
                sum=sum-i
    return sum

print(all(n))
print(consec(n))
print(not_square(n))
