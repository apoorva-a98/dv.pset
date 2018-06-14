def sum_of_factors(n):
    sum=0
    for i in range(1,n,1):
        if n%i==0:
            #print(i)
            sum=sum+i
    return sum

def check_for_amicable():
    sum=0
    for i in range(1,10001,1):
        if sum_of_factors(sum_of_factors(i))==i:
            print(sum_of_factors(sum_of_factors(i)),"and",sum_of_factors(i))
            sum=sum+i
    return sum
print(check_for_amicable())
