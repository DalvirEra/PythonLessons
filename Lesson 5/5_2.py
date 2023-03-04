A = int(input("A = "))
B = int(input("B = "))

def sum(A,B):
    if B == 0:
        return A
    else:
        A+= 1
        B-= 1
        return sum(A,B)

print(sum(A,B))
