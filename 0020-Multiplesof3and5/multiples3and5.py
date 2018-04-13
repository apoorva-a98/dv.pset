def cal_multiples():
    i=3
    sum=0
    while(i<1001):
        if(i%3==0):
            sum=sum+i
        elif(i%5==0 and i%3!=0):
            sum=sum+i
        i=i+1
    return sum
print(cal_multiples())
