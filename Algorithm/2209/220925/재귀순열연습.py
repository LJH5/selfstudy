arr = [1, 2, 3]
sel = [0, 0, 0]
check = [0, 0, 0]

def perm(depth):
    if depth == 3:
        print(sel)
        return
    for i in range(3):
        if not check[i]:
            check[i] = 1
            sel[depth] = arr[i]
            perm(depth + 1)
            check[i] = 0

perm(0)