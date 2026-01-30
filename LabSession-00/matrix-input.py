row = int(input("Enter number of rows: "))
col = int(input("Enter number of cols: "))

matrix = []

for i in range(row):
    row_list = []
    for j in range(col):
        value = int(input("Enter value for position " + str(i) + " " + str(j) + ": "))
        row_list.append(value)
    matrix.append(row_list)

print(matrix)

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()