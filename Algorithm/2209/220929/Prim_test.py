def Prim():
    dist = [987654321]*(V+1)
    dist[V] = 0     # 맨 마지막을 선택
    visited = [False]*(V+1)

    for _ in range(V+1):
        min_idx = -1
        min_value = 987654321

        for i in range(V+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = True

        for i in range(V+1):
            if not visited[i] and adj[min_idx][i] < dist[i]:
                dist[i] = adj[min_idx][i]

    return sum(dist)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[987654321] * (V+1) for _ in range(V+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = adj[e][s] = w

    print(f'#{tc} {Prim()}')
