M=[]
name_file=open('names.txt','r')
items=name_file.read().split('","')
M=[str(i) for i in items]
#print(M)

'''def sort_by_length(Z):
    for j in range(len(Z)-1):
        for i in range(len(Z)-1):
            if(len(Z[i])>len(Z[i+1])):
                k=Z[i+1]
                Z[i+1]=Z[i]
                Z[i]=k
    return Z
print(sort_by_length(M))'''

def count(X,m):
    count=0
    for i in X:
        if len(i)>m-1:
            count=count+1
    return count

def check(a,b,n):
    flag=0
    for i in range(n):
        if a[i]==b[i]:
            flag=1
    return flag
print(check('able','abe',2))

def arrange_alphabetically(Z):
    n=3

    for j in range(len(Z)-1):
        for i in range(len(Z)-1):
            if(ord(Z[i][0])>ord(Z[i+1][0])):
                k=Z[i+1]
                Z[i+1]=Z[i]
                Z[i]=k

    for j in range(len(Z)-1):
        for i in range(len(Z)-1):
            if(ord(Z[i][0])==ord(Z[i+1][0]) and ord(Z[i][1])>ord(Z[i+1][1])):
                k=Z[i+1]
                Z[i+1]=Z[i]
                Z[i]=k

    for j in range(count(Z,n)):
        for i in range(len(Z)-1):
            if len(Z[i])>(n-1):
                print(Z[i]," ",end='')
                flag=0
                t=1
                while(flag==0):
                    if (i+t)>len(Z)-1:
                        break
                    elif len(Z[i+t])>(n-1) and check(Z[i],Z[i+t],n-1)==1 and ord(Z[i][n-1])>ord(Z[i+t][n-1]) and i+t<len(Z)-1:
                        print(Z[i+t])
                        k=Z[i+t]
                        Z[i+t]=Z[i]
                        Z[i]=k
                        flag=1
                    else:
                        t=t+1
            else:
                print("")


    return Z
print(arrange_alphabetically(M))
