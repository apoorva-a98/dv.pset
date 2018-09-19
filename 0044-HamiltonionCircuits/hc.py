L=['A','B','C','D','E']
E=[['A','B'],['A','E'],['C','B'],['C','D'],['D','E'],['A','D'],['C','E']]

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

'''def sqr(x):
    s=x**2
    return s

def sqrt(x):
    s=x**0.5
    return s

def dist(A,B):
    distance=sqrt(sqr(B[1]-A[1])+sqr(B[2]-A[2]))
    return distance'''

#permutations
def permutations(M):
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
    #print(len(B))
    return B

#print(permutations)

#checking for edges
def is_within(a,b,e):
    flag=1
    for i in e:
        #print(i[0],i[1])
        if (a==i[0] and b==i[1]) or (a==i[1] and b==i[0]):
            return 1
    return 0

print(is_within('D','C',E))

#circuits
def circuits(M,e):
    N=permutations(M)
    #print(N)
    N2 = []
    #magic = 0
    #print('length of N', len(N))
    for index,i in enumerate(N):
        #print('magic is', magic)
        for j in range(len(i)):
            node=is_within(i[j],i[(j+1)%(len(i))],e)
            #print(i[j],i[(j+1)%(len(i))],e)
            #print(node)
            if node==0:
                #print("Removing " + str(i))
                #N.pop(index)
                #magic = magic+1
                break
        if node==1:
            N2.append(N[index])
        #print("clear",i)

    return "all the hameltonion circuits",N2

print(circuits(L,E))








'''def circuits(M,e):
    N=permutations(M)
    print(N)
    #index=0
    for i in N:
        #node=1
        for j in range(len(i)):
            node=is_within(i[j],i[(j+1)%(5)],e)
            #print(i[j],i[(j+1)%(5)],e)
            #print(node)
            if node==0:
                #t=O.index(i)
                #print(t)
                #print(index,N[index])
                N.remove(i)
                break
        #if node==1:
            #print("clear",index,N[index])
            #index=index+1
    return N'''







'''for i in range(len(B)):
    B[i].append(B[i][0])
print("ALL CIRCUITS: ",B,len(B))

#hemeltonion starts here
    for j in range(len(B)):
        s=0
        t=len(B[j])
        flag=0
        while(s<t):
            for i in range(s+2,s+2+t-1,1):
                print('i',i%t,'s',s,'j',j,'t',t,'s+2+t-1',s+2+t-1)
                if((dist(B[j][s],B[j][i%t])+dist(B[j][s+1],B[j][i%t]))==dist(B[j][s],B[j][s+1])):
                    #B.pop(j)
                    print(B[j][s],B[j][s+1],B[j][i%t],dist(B[j][s],B[j][i%t]),dist(B[j][s+1],B[j][i%t]),dist(B[j][s],B[j][s+1]))
                    flag=1
                    print("flag")
                    break
                if flag==1:
                    break
            s=s+1
            if flag==1:
                break
    return B,len(B)

    u=len(B)
    i=0
    l=len(B[0])-1
    m=len(B[0])
    print(l)
    while(i<u):
        flag=0
        if((dist(B[i%m][0],B[i%m][1])+dist(B[i%m][0],B[i%m][2]))==dist(B[i%m][1],B[i%m][2])):
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
    return B,len(B)'''

#print(hameltonion_circuit(L))
