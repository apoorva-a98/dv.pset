def check_palandrome(no):
    orig=no
    reverse=0
    while(no>0):
        x=no%10
        reverse=reverse*10+x
        no=no//10
    if(orig==reverse):
        flag=1
    else:
        flag=0
    return flag

def Bubble_sort(L):
    for j in range(len(L)-1):
        for i in range(len(L)-1):
            if(L[i]<L[i+1]):
                k=L[i+1]
                L[i+1]=L[i]
                L[i]=k
    return L

def largest_product():
    F=[]
    for i in range(999,900,-1):
        for j in range(999,900,-1):
            number=i*j
            check=check_palandrome(number)
            if(check==1):
                F.append(number)
    Bubble_sort(F)
    print(F)
    print(F[0])

largest_product()
