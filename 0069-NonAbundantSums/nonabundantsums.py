print ("please wait, the solution takes time!")
def sumOfProperDivisors(x):
    sum=0
    for i in range (1,x):
        if x%i==0:
            sum=sum+i
    return sum
A=[]
def checkAbundant():
    for i in range (1,28123):
        if sumOfProperDivisors(i)>i:
            A.append(i)
    return A
checkAbundant()
#sum of int+ that can be written as sum of 2abunNo
B=[]
def sumOfTwoAbundantNos():
    b=0
    for i in range (len(A)):
        for j in range (i+1,len(A)):
            b=A[i]+A[j]
            B.append(b)
    return B
sumOfTwoAbundantNos()
def bubbleSort(B):
    for i in range(len(B)):
        for j in range(i+1):
                if B[i]>B[j]:
                    z=B[i]
                    B[i]=B[j]
                    B[j]=z
    return(B)
bubbleSort(B)
summ=0
for i in range (1,28123):
    if i not in B: #i not in list B
        summ=summ+i
        print (i," ",summ)
print ('sol',summ)
'''find sum of all positive integers which cannot
be written as the sum of two abundant numbers
#integers less than 28123 cant be written as the sum
#of two abundant numbers
'''
