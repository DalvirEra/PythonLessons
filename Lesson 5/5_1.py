A = int(input("A = "))
B = int(input("B = "))

def mult(A,B,C):
    if C == B:
        return A
    else:
        return A * mult(A,B,C+1)

print(mult(A,B,1))
