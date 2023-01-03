rows_cols_input = input().split(", ")

matrix = []

rows = int(rows_cols_input[0])
cols = int(rows_cols_input[1])
total_sum = 0

for i in range(rows):
    current = input().split(", ")
    current = [int(n) for n in current]
    current_sum = sum(current)
    total_sum += current_sum
    matrix.append(current)

print(total_sum)
print(matrix)
