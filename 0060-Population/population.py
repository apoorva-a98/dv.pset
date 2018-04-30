A=50000000
B=70000000

def inc(M):
    M=M+(0.03*M)
    return M

def incr(N):
    N=N+(0.02*N)
    return N

def population(M,N):
    year=0
    while(M<N):
        M=inc(M)
        N=incr(N)
        print(M,N)
        year=year+1
    print(str(year)+"years!")

population(A,B)
