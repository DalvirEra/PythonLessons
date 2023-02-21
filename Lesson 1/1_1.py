m = int(input("Число: "))
summ = 0

while m>1:
    summ += int(m%10)
    m = m/10

print(summ)
