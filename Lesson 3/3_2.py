# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

number = int(input("n: "))
listNums = []
for each in range(0, number):
    listNums.append(int(input()))

X = int(input("x: "))
Closest = 999

for each in range(len(listNums)):
    if abs(listNums[each] - X) < abs(Closest - X) :
        Closest = listNums[each]

print(Closest)