matrix = [[1, 8, 4], 
		  [7, 3, 9], 
		  [5, 2, 6]]

flag = False

for r in range(3):
    for c in range(3):
        if matrix[r][c] == 3:
            flag = True
            break
        else:
            print(matrix[r][c], end=' ')
    
    if flag:
        break