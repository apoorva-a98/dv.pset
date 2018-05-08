def initialize(x): #initializing primary numbers
     D={0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
     11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',
     18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',
     70:'Seventy',80:'Eighty',90:'Ninety',100:'Hundred'}
     #print("inside initialize func:: x is " + str(x))
     return D[x]

a=int(input("enter a no less than 999999: ")) #take input

def recogonize(no): #count the number of digits
    count=0
    while(no>0):
        if((no//10)>0):
            count=count+1
        no=no//10
    count=count+1
    return count

def breakup(no): #final function to display numbernames
    test=recogonize(no)
    due=test
    i=1
    for j in range(1,test,1):
        i=i*10
    flag=0
    slag=0

    while(test>1): #units, tents, etc. places
        b=no//i

        if(test==9):
            prt=" hundred"
        elif(test==8):
            prt=initialize(b*10)
        elif(test==7):
            prt=" million"
        elif(test==6):
            prt=" hundred"
        elif(test==5):
            prt=initialize(b*10)
        elif(test==4):
            prt=" thousand"
        elif(test==3):
            prt=" hundred"
        elif(test==2):
            prt=initialize(b*10)
        else:
            prt=""

        if(b==0 and due>6 and test>6):
            print("Million ",end="")
            flag=1
        elif(b==0 and due>6):
            print("",end="")
        elif(b==0 and due<6 and due>3 and test>3):
            print("Thousand ",end="")
            slag=1
        elif(b==0 and due<6 and due>3):
            print("",end="")
        elif(b==0 and test==3):
            print("",end="")
        elif(test==2 or test==5 or test==8):
            print(prt+str(" "),end="") #for 10s place
        else:
            print(initialize(b)+prt+str(" "),end="") #printing the number name
        no=no%i
        i=i/10
        test=test-1
    print(initialize(no))

breakup(a) #calling the main function
