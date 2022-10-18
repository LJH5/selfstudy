def perm(depth):
    if depth == N:
        print(sel)
        return
    for i in range(N):
        if not check[i]:
            check[i] = 1
            sel[depth] = arr[i]
            perm(depth+1)
            check[i] = 0


N = int(input())
arr = [i for i in range(N)]
sel = [0]*N
check = [0]*N

perm(0)