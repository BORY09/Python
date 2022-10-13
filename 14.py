def RemoveDuplicates(list):
    x=[]
    for i in list:
        if i not in x:
            x.append(i)
    return x
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
print(len(a))

print(RemoveDuplicates(a))
print(len(RemoveDuplicates(a)))

lista = set(a)
lista=list(lista)
print(lista)
