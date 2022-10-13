def rev(lista):
    x = lista.split()
    result = []
    for word in x:
        result.insert(0,word)
    return ' '.join(result)

def reversedWord(word):
    return ' '.join(word.split()[::-1])

a = 'My name is Michele'
b = rev(a)
c = reversedWord(a)
print(b)
print(c)

