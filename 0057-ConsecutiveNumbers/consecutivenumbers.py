x=int(input("give tthe number of lines"))

def consecutive_numbers(y):
    no=1
    for i in range(y+1):
        for j in range(0,i,1):
            print(no,end=''+" ")
            no=no+1
        print("\n")
consecutive_numbers(x)
