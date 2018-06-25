L=['A','B','C','D']

#sends the last item to the first position(0th index) and shifts everything else to the right
def rotate(M):
    last=len(M)-1
    temp=M[last]
    for i in range(last,0,-1):
        M[i]=M[i-1]
    M[0]=temp
    return M

#returns factorial
def factorial(n):
    fact=1
    for i in range(1,n+1,1):
        fact=fact*i
    return fact
print(factorial(3))

def hameltonion_circuit(M):
    i=1
    B=[]
    B.append([M[0]]) #appending the value at the 0th index to a list within the list B
    while(i<=len(M)):
        #print(B)
        for list in B:
            list.append(M[i]) #will append the value at the i(th) position of M to all the lists within the list B
        print(B)
        #upper=factorial(i)
        #print(upper)
        #print(len(B))
        for k in range(len(B)): # will fisr run 1 then 2,6,24 etc.
            #print(B)
            #will take the list-rotate and append
            G=B[k]
            for l in range(i):
                #print(B) #this gives the output as [['A','B']]
                #B.append(G)
                B.append(rotate(G)) # this by y understanding should give[['A','B'],['B','A']] but is giving [['B','A'],[none]]
                print(B)
        i=i+1
        print("\n")
    return B



'''def hameltonion_circuit(M):
    i=1
    B=[]
    B.append([M[0]])
    while(i<=len(M)):
        for list in B:
            list.append(M[i])
        for k in range(len(B)):
            G=B[k]
            for l in range(i):
                B.append(rotate(G))
                print(B)
        i=i+1
    return B

print(hameltonion_circuit(L))



M=['A','B','C']

def hameltonion_circuit():
    B=[]
    B=M[[0]]
    i=1
    while(i<3):
        for all the lists within the list B:
            append M[i]
        for no the number of lists present:
            take one list at a time
            for as many times as i:
                rotate the list taken
        i=i+1






G.append(M)
    A=2
    B=factorial(A)*-1
    for i in range(23):
        while(A<len(M)+1):
            take=M[B]
            for i in range(B,len(M)-1,1):
                M[i]=M[i+1]
            M[-1]=take
            A=A+1
        G.append(M)
    return G

print(hemeltonion_circuit(L))'''
