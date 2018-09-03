A=[0,0,0,0,1,1,1,1]
B=[0,0,1,1,0,0,1,1]
Cin=[0,1,0,1,0,1,0,1]

def xor(x,y):
    z=not((x and y)or not(x or y))
    return z

def adder2(a,b,cin):
    SUM=[]
    COUT=[]
    for i in range(8):
        t=xor(xor(a[i],b[i]),cin[i])
        if t:
            SUM.append(1)
        else:
            SUM.append(0)
        COUT.append((a[i] and b[i]) or (b[i] and cin[i]) or (a[i] and cin[i]))
    return SUM,COUT

print(adder2(A,B,Cin))
