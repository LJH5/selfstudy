import sys; sys.stdin = open('14413.txt')



for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    Q = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] != '?':
                Q.append([r, c])

    ans = 'possible'
    while Q and ans == 'possible':
        r, c = Q.pop(0)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if arr[nr][nc] == arr[r][c]:
                ans = 'impossible'
                break
            if arr[nr][nc] == '?':
                arr[nr][nc] = '#' if arr[r][c] == '.' else '.'
                Q.append([nr, nc])

    print(f'#{tc} {ans}')