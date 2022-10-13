a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random
a = random.sample(range(1,100),10)

b = random.sample(range(1,100),15)

def CommonElementsInLists(a,b):
    c = []
    x=a
    if(len(a)<len(b)):
       x=a
       y=b
    else:
        x=b
        y=a
    for i in y:
       if(i in x):
          c.append(i)

    print(c)

def CommonElements(a,b):
        print([num for num in b if num in a])

print(a)
print(b)
CommonElementsInLists(a,b)

CommonElements(a,b)
