import sys; sys.stdin = open('11012.txt')


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for _ in range(M):
        sr, sc, wh = map(int, input().split())

        for r in range(sr, min(sr + wh, N)):
            for c in range(sc, min(sc + wh, N)):
                ans += arr[r][c]
                arr[r][c] = 0

    print(f'#{tc} {ans}')
