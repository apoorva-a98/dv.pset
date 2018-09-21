L=['A','B','C','D','E']
E=[['A','B',2],['A','E',3],['C','B',4],['C','D',5],['D','E',6],['A','D',7],['C','E',8]]

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

#print(is_within('D','C',E))

#circuits
def circuits(M,e):
    N=permutations(M)
    HC = []
    for index,i in enumerate(N):
        for j in range(len(i)):
            node=is_within(i[j],i[(j+1)%(len(i))],e)
            if node==0:
                break
        if node==1:
            HC.append(N[index])
    return HC
#print(circuits(L,E))


def calculate_distance(M,e):
    sum=0
    for i in range(len(M)):
        for j in e:
            if (M[i]==j[0] and M[(i+1)%len(M)]==j[1]) or (M[i]==j[1] and M[(i+1)%len(M)]==j[0]):
                sum=sum+j[2]
    return sum
#print(calculate_distance(L,E))

def travelling_routes(M,e):
    h_cycles=circuits(M,e)
    min=calculate_distance(h_cycles[0],e)
    TR=[]
    for i in h_cycles:
        dist=calculate_distance(i,e)
        if dist<=min:
            min=dist

    for index,j in enumerate(h_cycles):
        if calculate_distance(j,e)==min:
            TR.append(h_cycles[index])
            h_cycles[index].append(calculate_distance(j,e))
    return 'all minimum travelling routes', TR
print(travelling_routes(L,E))
