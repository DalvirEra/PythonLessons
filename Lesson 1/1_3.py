m = input("Число: ")
part1 = int(m[0])+int(m[1])+int(m[2])
part2 = int(m[-1])+int(m[-2])+int(m[-3])
if part1 == part2:
    print("Yes")
else:
    print("No")
