L=[['A',2,2],['B',4,2],['C',6,2],['D',4,6],['E',6,6]]

def rotate(M):
    last=len(M)-1
    temp=M[last]
    for i in range(last,0,-1):
        M[i]=M[i-1]
    M[0]=temp
    return M

def factorial(n):
    fact=1
    for i in range(1,n+1,1):
        fact=fact*i
    return fact

def sqr(x):
    s=x**2
    return s

def sqrt(x):
    s=x**0.5
    return s

def dist(A,B):
    distance=sqrt(sqr(B[1]-A[1])+sqr(B[2]-A[2]))
    return distance

def hameltonion_circuit(M):
    i=1
    B=[]
    B.append([M[0]])
    while(i<len(M)):
        for b in B:
            b.append(M[i])
        upper=factorial(i)
        for k in range(upper):
            G=B[k][:]
            for l in range(i):
                g = rotate(G)[:]
                B.append(g[:])
        i=i+1

    for i in range(len(B)):
        B[i].append(B[i][0])
    print("ALL CIRCUITS: ",B,len(B))

    u=len(B)
    i=0
    l=len(B[0])-1
    print(l)
    while(i<u):
        flag=0
        if((dist(B[i][0],B[i][1])+dist(B[i][0],B[i][2]))==dist(B[i][1],B[i][2])):
            B.pop(i)
            u=u-1
            continue
        elif((dist(B[i][l-2],B[i][l-1])+dist(B[i][l-2],B[i][l]))==dist(B[i][l],B[i][l-1])):
            B.pop(i)
            u=u-1
            continue
        for j in range(2,u-1,1):
            for k in range(j-1):
                if ((dist(B[i][k],B[i][j])+dist(B[i][k+1],B[i][j]))==dist(B[i][k],B[i][k+1])):
                    flag=1
                    B.pop(i)
                    u=u-1
                    i=i-1
                    break
                elif ((dist(B[i][k],B[i][k+1])+dist(B[i][k],B[i][j]))==dist(B[i][j],B[i][k+1])):
                    flag=1
                    B.pop(i)
                    u=u-1
                    i=i-1
                    break
                elif ((dist(B[i][k],B[i][k+2])+dist(B[i][k],B[i][k+3]))==dist(B[i][k+3],B[i][k+2])):
                    flag=1
                    B.pop(i)
                    u=u-1
                    i=i-1
                    break
            if flag==1:
                break
        i=i+1
    return B,len(B)

print(hameltonion_circuit(L))
