import sys
sys.stdin = open('input.txt', 'r')

def find(now):
    global result

    r, c = now
    if (r, c) not in visited:
        visited.add((r, c))
    if maze[r][c] == 3:
        result = 1
        return
    for k in range(4):
        next_r = r + dr[k]
        next_c = c + dc[k]
        if 0 <= next_r < N and 0 <= next_c < N and (next_r, next_c) not in visited and maze[next_r][next_c] != 1:
            find((next_r, next_c))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0
    maze = [list(map(int, input())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = set()
    # 시작점(2)의 인덱스를 찾아라
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)

    find(start)
    print(f'#{tc} {result}')