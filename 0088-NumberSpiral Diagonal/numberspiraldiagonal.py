def sum_of_diagonals():
    i,j,k,sum=1,2,0,0
    while(i<(1001*1001)+1):
        sum=sum+i
        #print(i)
        i=i+j
        k=k+1
        if k%4==0:
            j=j+2
    return sum
print(sum_of_diagonals())
