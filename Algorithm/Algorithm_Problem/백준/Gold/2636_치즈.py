from collections import deque
# 바깥쪽 공기가 닿지 않는 곳이 치츠의 안의 공기


def air_idx():
    air_set = set()
    q = deque()
    q.append((0, 0))
    air_set.add((0, 0))
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                if cheese[nr][nc] == 1 or (nr, nc) in air_set:
                    continue
                if cheese[nr][nc] == 0:
                    air_set.add((nr, nc))
                    q.append((nr, nc))
    melt(air_set)


def melt(air):
    for r, c in air:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if cheese[nr][nc] == 1:
                cheese[nr][nc] = 0


def cheese_cnt():
    cnt = 0
    for r in range(1, N-1):
        for c in range(1, M-1):
            if cheese[r][c] == 1:
                cnt += 1
    return cnt


N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

time = 0
last_cheese = 0

while True:
    last_cheese = cheese_cnt()
    air_idx()
    time += 1
    if cheese_cnt() == 0:
        break


print(time)
print(last_cheese)
