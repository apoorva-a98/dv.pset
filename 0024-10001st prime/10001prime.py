def prime(n):
    test=0
    for i in range(2,n,1):
        if(n%i==0):
            test=0
            break
        else:
            test=1
    return test
print(prime(16))

def tenthousandandfirst():
    x=1
    sum=0
    print("wait for 2min")
    while(sum<10002):
        check=prime(x)
        if(check==1):
            sum=sum+1
        x=x+1
    print(x)
tenthousandandfirst()
