M=[6,1,1901]

def next_d(N):
    N[0]=N[0]+1
    if((N[1]==4 or N[1]==6 or N[1]==9 or N[1]==11) and N[0]>30):
        N[1]=N[1]+1
        N[0]=N[0]%30
        if(N[1]>12):
            N[2]=N[2]+1
            N[1]=N[1]%12
    elif((N[1]==1 or N[1]==3 or N[1]==5 or N[1]==7 or N[1]==8 or N[1]==10 or N[1]==12) and N[0]>31):
        N[1]=N[1]+1
        N[0]=N[0]%31
        if(N[1]>12):
            N[2]=N[2]+1
            N[1]=N[1]%12
    elif(N[1]==2 and N[0]>28 and N[2]%4!=0):
        N[1]=N[1]+1
        N[0]=N[0]%28
        if(N[1]>12):
            N[2]=N[2]+1
            N[1]=N[1]%12
    elif(N[1]==2 and N[2]%4==0 and N[0]>28):
        if(N[2]%100!=0):
            N[0]=29
        elif(N[2]%100==0 and N[2]%400==0):
            N[0]=29
        else:
            N[1]=N[1]+1
            N[0]=N[0]%28
            if(N[1]>12):
                N[2]=N[2]+1
                N[1]=N[1]%12
    return N

def counting_sundays(N):
    count=0
    sunday=1
    while(N[2]!=2001):
        N=next_d(N)
        count=count+1
        if count%7==0:
            sunday=sunday+1
            print(N,"sunday")
    return count

print("the number of sundays: ",counting_sundays(M))
