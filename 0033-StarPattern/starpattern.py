x=int(input("give number "))
for m in range (0,x+1,1):
    for n in range (0,m,1):
        print("*",end="")
    print("\n")
print("\n")

for m in range (x+1,0,-1):
    for n in range (1, m, 1):
        print("*",end="")
    print("\n")
print("\n")

if(x%2==0):
    for m in range (0,int(x/2)+1,1):
        for n in range (0,m,1):
            print("*",end="")
        print("\n")
else:
    for m in range (0,int(x/2)+2,1):
        for n in range (0,m,1):
            print("*",end="")
        print("\n")
for m in range (int(x/2)+1,0,-1):
    for n in range (1, m, 1):
        print("*",end="")
    print("\n")
print("\n")
