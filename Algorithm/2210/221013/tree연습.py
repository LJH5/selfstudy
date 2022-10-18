'''
정점 번호: V = 13
간선 수: E = V - 1 = 12
부모-자식 순: 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def preorder(n):
    if n:
        print(n, end=' ')
        preorder(lc[n])
        preorder(rc[n])


V = 13
E = V - 1
arr = list(map(int, input().split()))
lc = [0] * (V + 1)
rc = [0] * (V + 1)
for i in range(E):
    p = arr[i * 2]
    c = arr[i * 2 + 1]
    if lc[p] == 0:
        lc[p] = c
    else:
        rc[p] = c

preorder(1)