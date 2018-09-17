name_file=open('largesum.txt','r')
items=name_file.read()
l=items.split('\n')

sum=0
for i in l:
    i=int(i)
    sum=sum+i
sum=str(sum)
print ('First ten digits of sum: ',sum[0:9])
