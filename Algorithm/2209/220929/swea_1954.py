# N*N 행렬
# 시계방향으로 회전 -> 우하좌상
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matirx = [[0]*N for _ in range(N)]
    # 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    num = 1
    r, c = 0, -1
    dir = 0
    while num <= N*N:
        for i in range(N):
            r = r + dr[dir]
            c = c + dc[dir]
            if 0 <= r < N and 0 <= c < N and not matirx[r][c]:
                matirx[r][c] = num
                num += 1
            # 범위를 벗어나면 방향을 바꿔야함
            else:
                r = r - dr[dir]
                c = c - dc[dir]
                dir = (dir + 1) % 4

    print(f'#{tc}')
    for line in matirx:
        print(*line)
