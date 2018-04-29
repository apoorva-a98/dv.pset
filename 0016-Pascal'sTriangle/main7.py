no=int(input("Enter no for pascal's triangle"))
def pascals_triangle1(num):
    a=[]
    for i in range(num):
        b=[]
        for j in range(i+1):
            if (j==0 or i==j):
                b.append(1)
                print("1",end=" ")
            else:
                val=((a[i-1][j-1])+(a[i-1][j]))
                b.append(val)
                print(val,end=" ")
        print("\n")
        #a.append(b)
    #print(a)
pascals_triangle1(no)

'''a=int(input("Enter no for pascal's triangle"))
def pascals_triangle1(x):
    for i in range(x):
        for k in range(x-1-i):
            print(" ",end="")
        for j in range(i+1):
            value=combination(i,j)
            print(value," ",end="")
        print("\n")

pascals_triangle1(a)'''
