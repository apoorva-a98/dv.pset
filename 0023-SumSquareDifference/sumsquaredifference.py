def sqr(n):
    s=n*n
    return s
print(sqr(2))

def sum_of_sqr():
    sum=0
    for i in range(101):
        sum=sum+sqr(i)
    return sum

def sqr_of_sum():
    sum=0
    for i in range(101):
        sum=sum+i
    result=sqr(sum)
    return(result)

print(sqr_of_sum()-sum_of_sqr())
