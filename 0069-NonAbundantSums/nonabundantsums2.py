def sum_of_factors(x):
    sum=0
    for i in range(1,x,1):
        if x%i==0:
            sum=sum+i
    return sum
#print(sum_of_factors(6))

def sum_of_abundant():
    L=[]
    sum=0
    for i in range(2,28124,1):
        if((i/2)%2==0 and sum_of_factors(i//2)>i//2):
            print(i," is sum of abundant number ",i/2)
        else:
            sum=sum+i
    return sum,"is the sum of all the positive integers which arn't a sum of two abundant num"
print("sum: ",sum_of_abundant())
