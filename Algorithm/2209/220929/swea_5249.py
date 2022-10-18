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
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    # 비용을 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])
    # 노드의 번호는 0번 부터
    p = [0]*(V+1)
    for i in range(V+1):
        make_set(i)
    result = 0
    cnt = 0

    for x, y, w in edges:
        if find_set(x) != find_set(y):
            union(x, y)
            result += w
            cnt += 1

    print(f'#{tc} {result}')
