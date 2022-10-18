import sys; sys.stdin = open('12712.txt')
dr1 = [-1, 0, 1, 0]  # 상우하좌
dc1 = [0, 1, 0, -1]
dr2 = [-1, -1, 1, 1]
dc2 = [-1, 1, 1, -1]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # + 모양
    for r in range(N):
        for c in range(N):
            # 기준점 r,c
            # 네방향에 대해서
            kill = arr[r][c]  # 기준점은 한번만
            for dir in range(4):
                for i in range(1, M):  # 기준점 제외하고 다음 칸부터
                    nr, nc = r + dr1[dir] * i, c + dc1[dir] * i
                    if 0 <= nr < N and 0 <= nc < N:
                        kill += arr[nr][nc]
            ans = max(ans, kill)

    # X 모양
    for r in range(N):
        for c in range(N):
            # 기준점 r,c
            # 네방향에 대해서
            kill = arr[r][c]  # 기준점은 한번만
            for dir in range(4):
                for i in range(1, M):  # 기준점 제외하고 다음 칸부터
                    nr, nc = r + dr2[dir] * i, c + dc2[dir] * i
                    if 0 <= nr < N and 0 <= nc < N:
                        kill += arr[nr][nc]
            ans = max(ans, kill)

    print(f'#{tc} {ans}')
