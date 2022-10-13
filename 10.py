import random


a = random.sample(range(10),5)
b = random.sample(range(10),10)
result = [i for i in a if i in b]
print(a)
print(b)
print(result)
