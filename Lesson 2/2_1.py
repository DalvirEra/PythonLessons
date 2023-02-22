import random

n = int(input("монетки: "))
x = random.randint(1, n)
y = n-x
print("Решка: ", x)
print("Орел: ", y)
if x < y:
    print("минимум: ", x)
else:
    print("минимум: ", y )




