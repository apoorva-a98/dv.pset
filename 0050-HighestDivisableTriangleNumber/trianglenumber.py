def count_of_divisors(n):
    count=0
    for i in range(1,n+1,1):
        if n%i==0:
            count=count+1
            #print(i)
    return count
#print(count_of_divisors(6))

def triangle_number():
    i=1
    sum=0
    while(i>0):
        sum=sum+i
        x=count_of_divisors(sum)
        if(x>500):
            print("triangle number",sum)
            break
        else:
            i=i+1
triangle_number()
