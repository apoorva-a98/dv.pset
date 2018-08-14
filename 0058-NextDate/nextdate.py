print("enter dd m yyyy")
items=input().split(' ')
M=[int(i) for i in items]

def next_date(N):
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
    print(N[0],N[1],N[2])

next_date(M)
