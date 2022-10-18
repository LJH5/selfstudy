# dfs
# 좌상에서 우하
# 오른쪽과 아래만 탐색
# 최소합
def dfs(r, c, acc):
    global result
    if acc >= result:
        return
    if (r, c) == (N-1, N-1):
        if result > acc:
            result = acc
            return
    for k in range(2):
        next_r = r + dr[k]
        next_c = c + dc[k]
        if 0 <= next_r < N and 0 <= next_c < N:
            dfs(next_r, next_c, acc+matrix[next_r][next_c])

T = int(input())
for tc in range(1, T+1):
    result = 9999999999
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = set()
    dr, dc = [1, 0], [0, 1]

    dfs(0, 0, matrix[0][0])

    print(f'#{tc} {result}')