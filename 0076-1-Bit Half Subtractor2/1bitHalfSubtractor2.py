X=[0,0,1,1]
Y=[0,1,0,1]
def oneBitHalfSubtractor(X,Y):
    D=[]
    B=[]
    for i in range (0,4):
        b = not X[i] and Y[i]
        if b:
            B.append(1)
        else:
            B.append(0)
    #    D.append(d)
    for i in range(0,4):
        d = not((X[i] and Y[i]) or (not (X[i] or Y[i])))
        if d:
            D.append(1)
        else:
            D.append(0)
#        B.append(b)
    return D,B
print(oneBitHalfSubtractor(X,Y))
