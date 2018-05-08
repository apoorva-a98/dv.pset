action = input("enter your action(+,-,*,/)")
def action1(a):
    if a=="+":
        take1 = int(input("enter first no."))
        take2 = int(input("enter second no."))
        sum=take1+take2
        print(sum)

    elif a=="-":
        take1 = int(input("enter first no."))
        take2 = int(input("enter second no."))
        difference=take1-take2
        print(difference)

    elif a=="*":
        take1 = int(input("enter first no."))
        take2 = int(input("enter second no."))
        product=take1*take2
        print(product)

    elif a=="/":
        take1 = int(input("enter first no."))
        take2 = int(input("enter second no."))
        quotient=take1/take2
        print(quotient)

    else:
        print("invalid entry")
action1(action)
