# 양 울타리
from collections import deque
# r: 9 c: 12
# r*c 행렬
# 델타 탐색으로 한칸 씩 이동하고
# visited에 저장
# 막히면 되돌아오기
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
r, c = map(int, input().split())
field = [list(input()) for _ in range(r)]
total_sheep = 0
sheep_idx = set()
total_wolf = 0
visited = set()
Q = deque()
for i in range(r):
    for j in range(c):
        if field[i][j] == 'o':
            total_sheep += 1
            sheep_idx.add((i, j))
        elif field[i][j] == 'v':
            total_wolf += 1

for y, x in sheep_idx:
    if (y, x) not in visited:            # 백트래킹 1
        Q.append((y, x))
        tmp_sheep = 1
        tmp_wolf = 0
        while Q:
            for _ in range(len(Q)):
                y, x = Q.popleft()
                for k in range(4):
                    next_y = y + dr[k]
                    next_x = x + dc[k]
                    if next_y < 0 or next_y >= r or next_x < 0 or next_x >= c:
                        continue
                    if field[next_y][next_x] == '#' or (next_y, next_x) in visited:
                        continue
                    if field[next_y][next_x] == 'o':
                        tmp_sheep += 1
                    elif field[next_y][next_x] == 'v':
                        tmp_wolf += 1
                    visited.add((next_y, next_x))
                    Q.append((next_y, next_x))

        if tmp_sheep <= tmp_wolf:
            total_sheep -= tmp_sheep
        else:
            total_wolf -= tmp_wolf

print(total_sheep, total_wolf)