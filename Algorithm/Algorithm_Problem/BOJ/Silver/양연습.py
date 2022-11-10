from collections import deque


def start():
    find_count()
    check()


def find_count():
    global wolf_cnt
    global sheep_cnt
    for i in range(R):
        for j in range(C):
            if field[i][j] == 'o':
                sheep_idx.add((i, j))
                sheep_cnt += 1
            elif field[i][j] == 'v':
                wolf_cnt += 1


def check():
    for idx in sheep_idx:
        if idx not in visited:
            bfs(idx)


def bfs(idx):
    global wolf_cnt
    global sheep_cnt
    q = deque()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    q.append(idx)
    tmp_sheep = 0
    tmp_wolf = 0
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if field[nr][nc] == '#' or (nr, nc) in visited:
                continue
            q.append((nr, nc))
            visited.add((nr, nc))
            if field[nr][nc] == 'o':
                tmp_sheep += 1
            if field[nr][nc] == 'v':
                tmp_wolf += 1

    if tmp_sheep > tmp_wolf:
        wolf_cnt -= tmp_wolf
    else:
        sheep_cnt -= tmp_sheep


R, C = map(int, input().split())
field = [list(input()) for _ in range(R)]
sheep_cnt = 0
sheep_idx = set()
wolf_cnt = 0
visited = set()

start()

print(sheep_cnt, wolf_cnt)




