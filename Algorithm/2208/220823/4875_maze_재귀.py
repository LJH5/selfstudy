# 미로 0은 통로 1은 벽
# 2에서 출발하여 3으로 도착
# 델타탐색

# DFS를 사용?
# 출발지 좌표를 미리 구한다

# 델타 탐색으로 가다가 갈림길이 나오면 stack에 저장한 뒤
# 스택에서 하나씩 꺼내서 이동

# 재귀?(재귀로 풀자)
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())
    start_r = 0
    start_c = 0
    maze = [[1] * n for _ in range(n)]
    for i in range(n):
        tmp = input()
        for j in range(n):
            if tmp[j] == '1':
                pass
            elif tmp[j] == '2':                         # 시작점
                maze[i][j] = int(tmp[j])
                start_r = i
                start_c = j
            else:
                maze[i][j] = int(tmp[j])

    visited = set()                                     # 방문한 곳을 저장

    def find(now_r, now_c):
        global result
        if maze[now_r][now_c] == 3:                     # 3을 찾았으면 종료
            result = 1
            return
        visited.add((now_r, now_c))                     # 방문한 곳에 저장
        for k in range(4):                              # 시작점에서 텔타 탐색
            next_r = now_r + dr[k]
            next_c = now_c + dc[k]

            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= n:      # 영역을 벗어나면
                continue
            if maze[next_r][next_c] == 1 or (next_r, next_c) in visited:    # 벽이거나 방문한 곳 이라면
                continue
            find(next_r, next_c)

    find(start_r, start_c)

    print(f'#{tc} {result}')