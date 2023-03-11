def print_operation_table(operation, num_rows=6, num_columns=6):
    array = [1,2,3,4,5,6]
    sec = []
    for a in range(num_columns):
        for i in range(num_rows):
            sec.append(operation(array[i],a+1))
        print(*sec)
        sec = []


print_operation_table(lambda x, y: x * y)

print("\n#######\nВторой вариант решения веселее\n\n")

def print_operation_table2(operation, num_rows=6, num_columns=6):
    array = [1,2,3,4,5,6]
    [print(*list(map(operation,array, [each for i in range(num_columns)]))) for each in range(1,num_rows+1)]

print_operation_table2(lambda x, y: x * y)