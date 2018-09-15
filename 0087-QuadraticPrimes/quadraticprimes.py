#Final answer, after minutes of computing: Total Prime occurences 1011 a*b -60939 a -999 b 61
def quadPrime():
    a,b=1000,1001
    max=0
    coeff1,coeff2=0,0
    for i in range (-a+1,a):
        for j in range (-b,b+1):
            n=0
            count=0
            while prime((n**2)+(i*n)+j)==1:
                #print (count,(n**2)+(i*n)+j)
                count=count+1
                n=n+1
            if count>max:
                max=count
                coeff1=i
                coeff2=j
            print(count,max)
            print(" ")
    print ('Total Prime occurences',max,'a*b',coeff1*coeff2,'a', coeff1,'b',coeff2)

def prime(x):
    flag=0
    for i in range (2,x):
        if x%i == 0:
            flag=1
            return 0
    if flag==0:
        return 1

print(quadPrime())
