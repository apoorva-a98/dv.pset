N=int(input("Enter Numerator"))
D=int(input("Enter Denominator"))
M=int(input("Enter Numerator2"))
E=int(input("Enter Denominator2"))

def calculate_fraction(n,d,m,e):
    top=n+m
    bottom=d+e
    i=2
    while(i<=bottom):
        if(top%i==0 and bottom%i==0):
            top=int(top/i)
            bottom=int(bottom/i)
        else:
            i=i+1
    return(str(top)+"/"+str(bottom))

print(calculate_fraction(N,D,M,E))
