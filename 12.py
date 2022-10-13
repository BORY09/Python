def listEnds(list):
    x=[]
    x.append(list[0])
    x.append(list[len(list)-1])
    return x
def listEnds2(list):
    
    return [(list[0]), (list[len(list)-1])]
a = [5, 10, 15, 20, 25]
print(listEnds(a))
print(listEnds2(a))
