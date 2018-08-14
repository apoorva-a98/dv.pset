A=[1,2,3,4,5,6,7]
B=[3,4,5,6]

def symmetric_difference(P,Q):
    '''
    union of two sets minus their intersection
    Returns a set P (Python list) which is P SYM_DIFF Q
    '''
    R=[]
    P=[]
    R=(union(P,Q))
    P=(difference(P,Q))
    return R,P
print(symmetric_difference(A,B))
