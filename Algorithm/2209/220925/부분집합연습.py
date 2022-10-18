arr = [1, 2, 3]
check = [0, 0, 0]

def powerset(idx):

    if idx == 3:
        result = []
        for i in range(3):
            if check[i] == 1:
                result.append(arr[i])
        print(result)
        return

    for j in range(2):
        check[idx] = j
        powerset(idx + 1)

powerset(0)