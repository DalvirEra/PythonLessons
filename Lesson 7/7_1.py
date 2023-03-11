Stih = input("Стих: ").split()
n = []
for each in Stih:
    n.append(each.count("а"))
if n.count(n[0]) == len(n):
    print("Парам пам-пам")
else:
    print("Пам парам")
