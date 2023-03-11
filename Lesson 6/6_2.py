import random
list_1 = []
for n in range(10):
    list_1.append(random.randint(-20,20))
print(list_1)
min_number = int(input("Мин: "))
max_number = int(input("Макс: "))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)