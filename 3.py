a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
x = 34
def LessThan5(a):
    for i in a:
        if i<5:
           print(i) 
       

def ListLessThan5(a):
        b = []
        for i in a:
            if i < 5:
                b.append(i)
        print(b)
def ListLessThanX(x, a):
        b = []
        for i in a:
            if i < x:
                b.append(i)
        print(b)

LessThan5(a)
ListLessThan5(a)

ListLessThanX(x,a)

            
