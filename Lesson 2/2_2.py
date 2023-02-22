x = int(input())
y = int(input())
#Honestly just dont want to do real math
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)