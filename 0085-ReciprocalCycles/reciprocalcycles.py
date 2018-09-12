from decimal import *
getcontext().prec = 1000
def checkRecurring():
    max=0
    top=0
    index=0
    for i in range (2,1000):
        original=(Decimal(1)/Decimal(i))
        n=list(str(original))
        #print (original)
        #print (n)
        n.pop(0)
        n.pop(0)
        difference=0
        flag=0
        for j in range (len(n)):
            for k in range (j+1,len(n)):
                if n[j]==n[k]:
                    difference=k-j
                    #print(j,k,k+difference)
                    #print(n[j],n[k],n[k+difference])
                    #print(original)
                    #print ('m',k+difference,len(n))
                    if (k+difference<len(n) and n[j]==n[k+difference]):
                        if (difference>max):
                            max=difference
                            top=original
                            index=i
                        flag=1
                        break
            if flag==1:
                break
    print (original,'Maximum Recurrance:',max,'Number:',index,', 1/',index,top)
checkRecurring()
