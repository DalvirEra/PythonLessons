n = int(input("Сторона: "))
m = int(input("Сторона: "))
k = int(input("Дольки: "))

if ((k%n == 0) and (k< n*m)):
    print("Yes")
elif ((k%m == 0) and (k< n*m)):
    print("Yes")
else:
    print("No")

