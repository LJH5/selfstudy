import sys
import heapq


def dij():
    dist = [987654321 for _ in range(v + 1)]
    dist[start_node] = 0
    q = []
    heapq.heappush(q, (0, start_node))
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue
        for destination in adj[node]:
            cost = dist[node] + destination[0]
            if cost < dist[destination[1]]:
                dist[destination[1]] = cost
                heapq.heappush(q, (cost, destination[1]))

    return dist


v, e = map(int, sys.stdin.readline().split())
start_node = int(input())
adj = [[] for _ in range(v + 1)]
for _ in range(e):
    start, end, w = map(int, input().split())
    adj[start].append((w, end))


result = dij()
for idx in range(1, len(result)):
    if result[idx] == 987654321:
        result[idx] = 'INF'
    print(result[idx])