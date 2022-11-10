import sys


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cost_arr = [[0]*m for _ in range(n)]
cost_arr[0][0] = arr[0][0]

dr = [0, 1, 1]
dc = [1, 1, 0]

for r in range(n):
    for c in range(m):
        for k in range(3):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if cost_arr[nr][nc] < cost_arr[r][c] + arr[nr][nc]:
                cost_arr[nr][nc] = cost_arr[r][c] + arr[nr][nc]

print(cost_arr[-1][-1])