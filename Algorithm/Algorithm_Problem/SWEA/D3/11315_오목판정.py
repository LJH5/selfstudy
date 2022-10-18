def find_stone():
    global stones_point
    for i in range(N):
        for j in range(N):
            if table[i][j] == 'o':
                stones_point.add((i, j))

def check(r, c):
    global result
    dr = [1, 0, -1, 0, 1, 1, -1, -1]
    dc = [0, 1, 0, -1, 1, -1, -1, 1]
    for k in range(8):
        cnt = 0
        for i in range(N):
            nr = r + dr[k] * i
            nc = c + dc[k] * i
            if 0 <= nr < N and 0 <= nc < N:
                if table[nr][nc] == 'o':
                    cnt += 1
                else:
                    break
        if cnt >= 5:
            return 'YES'

for tc in range(int(input())):
    N = int(input())
    table = [list(input()) for _ in range(N)]
    stones_point = set()
    find_stone()
    result = 'NO'
    for r_point, c_point in stones_point:
        if check(r_point, c_point):
            result = 'YES'
            break
    print(f'#{tc+1} {result}')