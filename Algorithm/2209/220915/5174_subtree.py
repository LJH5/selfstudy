# E(간선의 개수) N(시작 노드)
def preorder(n):
    global result
    if n:
        result.append(n)                        # 전위 순회하여 부모 및 자식 저장
        preorder(lc[n])
        preorder(rc[n])


T = int(input())
for tc in range(1, T+1):
    result = []
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1       # 노드의 수

    lc = [0] * (V + 1)
    rc = [0] * (V + 1)

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if lc[p] == 0:
            lc[p] = c
        else:
            rc[p] = c

    preorder(N)
    print(f'#{tc} {len(result)}')
