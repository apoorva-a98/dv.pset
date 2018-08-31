def d_powers():
    A=[]
    flag=0

    for i in range (2,101):
        for j in range(2,101):
            flag=0
            for k in range(len(A)):
                if i**j==A[k]:
                    flag=1
                    break
            if flag==0:
                A.append(i**j)
    A.sort()
    return A, len(A)

print(d_powers())
