num=int(input("Enter number to convert to binary:"))

def base_conversion(x):
    A=[]
    while x>0:
        if x%2==0:
            A.append(0)
        else:
            A.append(1)
        x=x//2
    #return A

    B=[]
    for i in range (len(A)-1,-1,-1):
        B.append(A[i])
    return B

print(base_conversion(num))
