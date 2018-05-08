x=int(input("enter the upper limit"))

def is_divisable(X):
    count=0
    for i in range(1,X,1):
        if (i%7==0):
            count=count+1
    return count

print(is_divisable(x))
