A=[1,2,3,4,5,6,7]
B=[3,4,5,6]

def union(P,Q):
    R=[]
    flag=0
    for i in range (len(P)):
        R.append(P[i])
    for j in range (len(Q)):
        for k in range(len(P)):
            if Q[j]==P[k]:
                flag=1
                break
        if flag==0:
            R.append(Q[j])
    return R
print ('union:',union(A,B))
