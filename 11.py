#num = int(input('Insert a number: '))
#a = [x for x in range(2, num) if num % x == 0]
#print(a)

def isPrime(num):
    isPrime = False
    if num > 0:
        for x in range(2, num - 1):
            if num % x != 0:
                continue
            elif num % x == 0:
                return False
        return True
    else:
        return False
for x in range(2,30):
    num = x
    print(str(x) + str(isPrime(num))) 

