number = int(input("Podaj liczbę: "))
num = int(input("Podaj num: "))
check = int(input("Podaj check: "))


def OddorEven(number):
    if(number % 2 ==0):
        print(str(number) + " jest liczbą parzystą")
    else:
        print(str(number) + " jest liczbą nieparzystą")
    
def Is4multiply(number):
    if(number % 4 == 0):
        print(str(number) + " jest wielokrotnością liczby 4")


def modulo(num, check):
    if(num % check == 0):
        print(str(num) + "jest podzielne przez " + str(check))

OddorEven(number)
Is4multiply(number)
modulo(num,check)
