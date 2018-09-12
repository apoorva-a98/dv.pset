def checkRecurring():
    max=0
    top=0
    index=0
    for i in range (1,1000):
        original=1/i
        n=list(str(1/i))
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
    print ('Maximum Recurrance:',max,'Number:',index,', 1/',index,top)
checkRecurring()
