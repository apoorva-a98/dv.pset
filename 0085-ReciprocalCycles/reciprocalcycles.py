def cycle_count(no):
    count=1
    for i in range(3,len(no),1):
        if no[i]==no[2]:
            return count
        else:
            count=count+1
print(cycle_count(str(0.14561)))

def check_recurring(no):
    flag=0
    for i in range(3,len(no),1):
        if no[i]==no[2]:
            flag=1
            break
    return flag

def reciprocal():
    max=0
    take_count=0
    max_number=0
    for i in range(2,1000,1):
        x=str(1/i)
        check=check_recurring(x)
        if check==1:
            take_count=cycle_count(x)
            print(i,x,take_count)
            if take_count>max:
                max=take_count
                max_number=i
    return "the max number: ",max_number,1/max_number,max

print(reciprocal())
