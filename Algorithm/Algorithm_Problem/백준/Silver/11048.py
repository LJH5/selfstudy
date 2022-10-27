# 이동하기
import heapq

def dijstra():
    dist = [[0] * M for _ in range(N)]
    visited = set()
    heap = []
    heapq.heappush(heap, (0, 0))
    dr = [1, 0, 1]
    dc = [0, 1, 1]
    while heap:
        r, c = heapq.heappop(heap)

        if (r, c) not in visited:
            dist[r][c] = maze[r][c]
            visited.add((r, c))

            for k in range(3):
                r += dr[k]
                c += dc[k]
                if (r, c) in visited:
                    continue
                if not(0 <= r < N and 0 <= c < M):
                    continue

                heapq.heappush(heap, (r, c))


N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
result = 0
dijstra()