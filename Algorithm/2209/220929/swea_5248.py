# 1~N번, M장의 신청서
def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    V, M = map(int, input().split())
    arr = list(map(int, input().split()))
    edges = []
    for i in range(M):
        edges.append([arr[2*i], arr[2*i+1]])
    p = [0] * (V+1)
    result = 0
    for i in range(V+1):
        make_set(i)

    for x, y in edges:
        if find_set(x) != find_set(y):
            union(x, y)

    # 보스로 안 바뀐 애들 보스로 바꿔주기
    for i in range(1, V+1):
        find_set(i)
    result = len(set(p)) - 1

    print(f'#{tc} {result}')
