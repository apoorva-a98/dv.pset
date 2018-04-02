x=int(input("enter first no "))
y=int(input("enter second no "))
a=[]
b=[]
d=[]

def breakup():
    global x
    global y
    i=1000
    while(i>1):
        a.append(x//i)
        b.append(y//i)
        x=x%i
        y=y%i
        i=i//10
    a.append(x)
    b.append(y)
    return a,b

print(breakup())

def reverse(given):
    e=[]
    for j in range(len(given)-1,-1,-1):
        e.append(given[j])
    return e

def cal():
    global d
    for i in range (3,-1,-1):
        c=[]
        carry=0
        for k in range(3,i,-1):
            c.append(0)
        for j in range (3,-1,-1):
            multiply_single=(a[i]*b[j])+carry
            carry=multiply_single//10
            reminder=multiply_single%10
            c.append(reminder)
        if(carry>0):
            c.append(carry)
        for l in range(i,0,-1):
                c.append(0)
        d.append(reverse(c))
    return d
print(cal())

def add():
    global d
    f=[]
    carry=0
    for i in range(len(d[3])):
        sum=carry+d[0][len(d[0])-1-i]+d[1][len(d[1])-1-i]+d[2][len(d[2])-1-i]+d[3][len(d[3])-1-i]
        carry=sum//10
        reminder=sum%10
        f.append(reminder)
    if(carry>0):
        f.append(carry)
    return(reverse(f))
print(add())
