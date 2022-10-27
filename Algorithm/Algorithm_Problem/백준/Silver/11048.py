# 이동하기
import heapq

def dijstra():
    dist = [987654321] * (N*M)
    visited = set()
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        distance, node = heapq.heappop(heap)
        if node not in visited:
            dist[node] = distance
            visited.add(node)

            for k in range(4)

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
dijstra()