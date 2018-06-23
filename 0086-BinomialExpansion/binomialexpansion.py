x=int(input("enter binomial expansion number"))

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
#x=str(factorial(100))

def binomial_expansion(X):
    for i in range(X+1):
        print(factorial(X)/(factorial(X-i)*factorial(i)),"x^",X-i,"y^",i," +",end='')

binomial_expansion(x)
