def divisors(a):
    i = 1
    flag = True
    x=[]
    while((i<=a)):
        if a % i != 0:
            flag = False
        else:
            x.append(i)

        i= i +1
    print(x)


a = 360
        
divisors(a)
