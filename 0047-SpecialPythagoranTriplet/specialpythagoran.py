def special():
    for c in range(1000,0,-1):
        for b in range(c-1,0,-1):
            for a in range(b-1,0,-1):
                if (a**2+b**2==c**2 and a+b+c==1000):
                    print(a,",",b,",",c)
                    print(a*b*c)
                    break
special()
