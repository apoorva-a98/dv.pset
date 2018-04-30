print("enter any number of items with a space")
items=input().split(' ')
M=[int(i) for i in items]

def sort(L):
    for j in range(len(L)-1):
        for i in range(len(L)-1):
            if(L[i]>L[i+1]):
                k=L[i+1]
                L[i+1]=L[i]
                L[i]=k
    return L

M=sort(M)
print(M)

def repeated_numbers(L):
    k=0
    for i in range(0,len(L),1):
        sum=0
        for j in range(i+k+1,len(L),1):
            k=0
            if(L[i]==L[j]):
                sum=sum+1
        if(sum>0):
            print(L[i])
            k=sum+1

print(repeated_numbers(M))
