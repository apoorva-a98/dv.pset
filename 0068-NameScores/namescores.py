M=[]
name_file=open('names.txt','r')
items=name_file.read().split('","')
M=[str(i) for i in items]

M.sort()
#print(M)
#A='simran'

def countLetterScore(a):
    letters="0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count=0
    for h in range (len(a)):
        for i in range(len(letters)):
            if letters[i]==a[h]:
                count=count+i

    return count
#print(countLetterScore(A))

def total(L):
    sum=0
    for i in range (len(L)):
        sum=sum+(countLetterScore(L[i])*i)
    return sum
print ('Sum:',total(M))
