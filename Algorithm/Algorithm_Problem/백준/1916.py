import sys
# 최소비용 구하기
# 다익스트라를 이용
def dijkstra():
    dist = [987654321] * (V+1)
    dist[start] = 0
    visited = [False] * (V+1)

    for _ in range(V+1):
        min_idx = -1
        min_value = 987654321

        for i in range(V+1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = True
        print(visited, dist)
        for i in range(V+1):
            if not visited[i] and dist[i] > adj[min_idx][i] + dist[min_idx]:
                dist[i] = adj[min_idx][i] + dist[min_idx]

    return dist[end]

V = int(input())
E = int(input())
adj = [[987654321] * (V+1) for _ in range(V+1)]
for i in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    adj[s][e] = w
start, end = map(int, input().split())

print(dijkstra())