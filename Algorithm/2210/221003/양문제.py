from collections import deque
r, c = map(int, input().split())
field = [list(input()) for _ in range(r)]
sheep_idx = set()
total_sheep = 0
total_wolf = 0
visited = set()
for i in range(r):
    for j in range(c):
        if field[i][j] == 'o':
            sheep_idx.add((i, j))
            total_sheep += 1
        elif field[i][j] == 'v':
            total_wolf += 1

# 사방탐색을 하여 양과 늑대를 찾는다
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque()
# 양의 좌표를 하나 꺼내어서
for y, x in sheep_idx:
    # 방문한 좌표가 아니라면
    if (y, x) not in visited:
        # 방문한 좌표로 붙이고
        q.append((y, x))
        # 한 울타리 영역 내의 양과 늑대의 수를 저장
        tmp_sheep = 1
        tmp_wolf = 0
        while q:
            for _ in range(len(q)):
                y, x = q.popleft()
                if (y, x) not in visited:
                    visited.add((y, x))
                for k in range(4):
                    ny = y + dr[k]
                    nx = x + dc[k]
                    if ny < 0 or ny >= r or nx < 0 or nx >= c:
                        continue
                    if field[ny][nx] == '#' or (ny, nx) in visited:
                        continue
                    if field[ny][nx] == 'o':
                        tmp_sheep += 1
                    elif field[ny][nx] == 'v':
                        tmp_wolf += 1
                    visited.add((ny, nx))
                    q.append((ny, nx))
        if tmp_sheep <= tmp_wolf:
            total_sheep -= tmp_sheep
        else:
            total_wolf -= tmp_wolf

print(total_sheep, total_wolf)