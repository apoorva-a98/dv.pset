import random

# read a number
A=int(input("enter N"))
print("the sqr root is",A**0.5)

def f(x,N):
    return (x*x - N)

def ff(x):
    return 2*x

def newton(x, N):
    return x - f(x,N)/ff(x)

# initial guess
x = random.uniform(0,A)

# print(y)

for i in range(10):
    x= newton(x, A)
    print((i,x))
