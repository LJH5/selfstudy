# 이동하기
def find(r, c, tmp_sum):
    global result
    if (r, c) == (N-1, M-1):    # 목적지에 도착
        if tmp_sum > result:    # 사탕의 합이 최대값보다 많으면
            result = tmp_sum    # 최대값 갱신
        return

    for k in range(3):          # 3방으로 탐색하여
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:   # 이동 좌표가 미로 안에 있으면
            if maze[nr][nc] < tmp_sum + maze[r][c]:
                maze[nr][nc] = tmp_sum + maze[r][c]


N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
result = 0
dr = [0, 1, 1]
dc = [1, 1, 0]

find(0, 0, maze[0][0])

print(result)