L=[1,3,6,2,4,9]

def Bubble_sort(L):
    for j in range(5):
        for i in range(5):
            if(L[i]>L[i+1]):
                k=L[i+1]
                L[i+1]=L[i]
                L[i]=k
    return L

print(Bubble_sort())
