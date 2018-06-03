#a=int(input("enter number for collatz"))
def collatz(no):
    sum=1
    while(no>1):
        if no%2==0:
            no=no//2
            sum=sum+1
        else:
            no=3*no+1
            sum=sum+1
    return sum
#print(collatz(a))

def largest():
    max=0
    take=0
    number=0
    for i in range(1,1000001,1):
        take=collatz(i)
        if(take>max):
            max=take
            number=i
    return number,max
print(largest())
