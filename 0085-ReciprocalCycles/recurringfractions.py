m=int(input("enter numerator"))
n=int(input("enter denominator"))

def recurring(x,y):
    print(x//y,".")
    take=str(x/y)
    take.pop(0)
    take.pop(0)
    length=len(take)
    number=(10**length)*take
    print(number)
recurring(m,n)
