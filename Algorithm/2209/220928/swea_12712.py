# 파리퇴치3
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly_matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 상우하좌
    cro_dr = [-1, 0, 1, 0]
    cro_dc = [0, 1, 0, -1]

    # 대각선
    x_dr = [-1, -1, 1, 1]
    x_dc = [-1, 1, 1, -1]

    for r in range(N):
        for c in range(N):
            kill_cnt = fly_matrix[r][c]
            for k in range(4):
                for i in range(1, M):
                    cro_nr = r + cro_dr[k] * i
                    cro_nc = c + cro_dc[k] * i
                    if 0 <= cro_nr < N and 0 <= cro_nc < N:
                        kill_cnt += fly_matrix[cro_nr][cro_nc]
            result = max(result, kill_cnt)

            kill_cnt = fly_matrix[r][c]
            for k in range(4):
                for i in range(1, M):
                    x_nr = r + x_dr[k] * i
                    x_nc = c + x_dc[k] * i
                    if 0 <= x_nr < N and 0 <= x_nc < N:
                        kill_cnt += fly_matrix[x_nr][x_nc]
            result = max(result, kill_cnt)
    print(f'#{tc} {result}')