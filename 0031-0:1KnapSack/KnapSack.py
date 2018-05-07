ORIG_LIST=[]
MOD_LIST=[]
N=[]
#List of available items to steal (index,value,weight,quantity)
def create_input(M,cap):
    cap=int(input("give the total number of items"))
    I=1
    for i in range(cap):
        L=[]
        V=int(input("enter value: "))
        W=int(input("enter weight: "))
        Q=int(input("enter quantity: "))
        L.append(I)
        L.append(V)
        L.append(W)
        L.append(Q)
        I=I+1
        M.append(L)
    print("the list of items, value, weight and quantity")
    print (M)
create_input(ORIG_LIST,N)

#To get maximum value of all available items
def calculateMax(orig_list):
    maximum=0
    for i in range (len(orig_list)):
        if (orig_list[i][1] >= maximum):
            maximum=orig_list[i][1]
    return i
print("list index with maximum value: ",end='')
print (calculateMax(ORIG_LIST))

#The new modified quantity and weight
def basicCal(orig_list,mod_list):
    maximum=(calculateMax(ORIG_LIST))
    value=orig_list[maximum][1]
    I=1
    for i in range (len(orig_list)):
        Y=[]
        quantity= orig_list[maximum][1]//orig_list[i][1]
        weight2= quantity*orig_list[i][2]
        Y.append(I)
        Y.append(value)
        Y.append(weight2)
        Y.append(quantity)
        I=I+1
        mod_list.append(Y)
    return mod_list

print("the modified list, normalizing to the max value")
print(basicCal(ORIG_LIST,MOD_LIST))

CAPACITY=int(input("capacity of your knapsack :"))
#To sort the new and then the original list
def insertion_sort(mod_list,orig_list):
    for j in range(len(mod_list)-1):
        for i in range(len(mod_list)-1):
            if(mod_list[i][2]>mod_list[i+1][2]):
                k=mod_list[i+1]
                mod_list[i+1]=mod_list[i]
                mod_list[i]=k

                l=orig_list[i+1]
                orig_list[i+1]=orig_list[i]
                orig_list[i]=l

#To be a smart thief
def calculate_knapsack(orig_list,mod_list,capacity):
    #F=[]
    insertion_sort(mod_list,orig_list)
    print("normalized list sorted to weight")
    print(mod_list)
    print("the original list sorted to weight")
    print(orig_list)

    while(capacity>=0 and len(orig_list)>0):
        i=0
        if (orig_list[i][3]*orig_list[i][2])<=capacity:
            print("item : " +str(orig_list[i][0])+ " of quantity : "+str(orig_list[i][3]))
            capacity=capacity-(orig_list[i][3]*orig_list[i][2])
            orig_list.pop(i)
        else:
            total=0
            quantity=0
            for j in range (1,orig_list[i][3]+1,1):
                if ((j*orig_list[i][2])<=capacity):
                    total=j*orig_list[i][2]
                    quantity=j
            print("item : " +str(orig_list[i][0])+" of quantity : "+str(quantity))
            capacity=capacity-total
            orig_list.pop(i)

print(calculate_knapsack(ORIG_LIST,MOD_LIST,CAPACITY))
