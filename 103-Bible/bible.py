name_file=open('bible.txt','r')
items=name_file.read()
avoid=[' ','.','?','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','|',"\n",';',':','<','>','/',',' ]
#print (items)

def tokenify(s):
    s=s.lower()
    buff = ''
    words=[]

    for i in s:
        if i in avoid:
            if buff != '':
                words.append(buff)
            buff = ''
        elif (buff is not None):
            buff += i
    if buff is not None:
        words.append(buff)
        buff=''
    return words
#print (tokenify(items))

def countList(K):
    K.sort()
    #print (K)
    A={}
    i=0
    while(len(K)>0):
        count=1
        j=1
        while(j<len(K) and K[i]==K[j]):
            count=count+1
            K.pop(j)
            #print (A)
        A[K[i]]=count
        #A.append(count)
        #B.append(K[i])
        K.pop(i)
        #print(len(K))
        #print(K[i],K[j],count,limit)
        count=1

    A = sorted(A.items(), key=operator.itemgetter(1), reverse=True)
    return A

B=countList(tokenify(items))
words = list(B.keys())
count = list(B.values())

plt.bar(range(len(B)),count,tick_label=words)
plt.show()
