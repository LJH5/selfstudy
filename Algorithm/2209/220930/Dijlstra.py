# 0 ~ N까지

def dij():
    dist = [987654231] * (V+1)
    dist[0] = 0
    visited = [False] * (V+1)

    for _ in range(V+1):
        min_idx = -1
        min_value = 987654321

        for i in range(V+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = True

        for i in range(V+1):
            if not visited[i] and dist[i] > adj[min_idx][i] + dist[min_idx]:
                dist[i] = adj[min_idx][i] + dist[min_idx]

    return dist[V]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[987654321]*(V+1) for _ in range(V+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w   # 다익스트라는 단반향이다
    print(f'#{tc} {dij()}')
