arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum = 0
for i in range(3):
    sum += arr[i][i]
print(sum)

sum = 0
for i in range(3):
    sum += arr[i][2-i]
print(sum)