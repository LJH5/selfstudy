import sys
sys.stdin = open('input.txt', 'r')


def find_way(now, cnt):
    global result
    r, c = now
    if  maze[r][c] == 3:
        result = min(cnt, result)
        return
    if now not in visited:
        visited.add(now)
    for k in range(4):
        next_r = r + dr[k]
        next_c = c + dc[k]
        if 0 <= next_r < N and 0 <= next_c < N and (next_r, next_c) not in visited and maze[next_r][next_c] != 1:
            find_way((next_r, next_c), cnt + 1)


T = int(input())
for tc in range(1, T+1):
    result = 9999
    N = int(input())        # N*N 행렬
    maze = [list(map(int, input())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = set()
    flag = False
    for i in range(N):      # 시작지점 찾기
        for j in range(N):   
            if maze[i][j] == 2:
                start = (i, j)
                flag = True
                break
        if flag:
            break
    find_way(start, -1)         # 자기 자신의 거리는 빼줘야함

    if result == 9999:
        result = 0

    print(f'#{tc} {result}')