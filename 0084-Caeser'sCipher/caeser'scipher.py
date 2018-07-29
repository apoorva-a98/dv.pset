take= input("enter a message")
num= input("enter caeser's key")

def caeser_cypher(y,n):
    for i in y:
        a=int(ord(i))
        b=((int(a)-97+int(n))%26)+97
        print(chr(b),end='')
    print("\n")

def decryp(y,n):
    for i in y:
        a=int(ord(i))
        b=((int(a)-97-int(n))%26)+97
        print(chr(b),end='')
    print("\n")

caeser_cypher(take,num)
decryp(take,num)
