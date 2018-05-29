p=int(input("Enter number : "))
q=int(input("Enter second number : "))
s=0
t=0

X=list(str(p))
L = list(map(int, X))

Y=list(str(q))
M = list(map(int, Y))
#adding the digits
def findSumOfDigits():
    global s
    for j in range (len(L)):
        s=s+L[j]
    print ('sum1=', s)
    global t
    for j in range (len(M)):
        t=t+M[j]
    print ('sum2=', t)
    return (s,t)
findSumOfDigits()

def check():
    if s==t:
        print ('true')
    else:
        print ('false')
check()
