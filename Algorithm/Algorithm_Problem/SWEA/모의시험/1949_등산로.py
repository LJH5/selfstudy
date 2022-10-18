import sys
sys.stdin = open('input.txt', 'r')
def dfs(r, c, K, depth):
    global result
    if K == 0 and depth <= result:
        return
    if result < depth:
        result = depth
    for k in range(4):                          # 사방탐색
        new_r = r + dr[k]
        new_c = c + dc[k]
        if 0 <= new_r < N and 0 <= new_c < N:   # 유효한 index라면
            dfs(new_r, new_c, K, depth+1)

T = int(input())
for tc in range(1, T+1):
    result = 0
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 델타 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    print(f'#{tc} {result}')
