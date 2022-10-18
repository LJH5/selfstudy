import sys; sys.stdin = open('1954.txt')

dr = [0, 1, 0, -1]  # 우(0)하(1)좌(2)상(3)우(0)....
dc = [1, 0, -1, 0]  # 방향 전환 dir = (dir + 1) % 4
N = 2
arr = [[0] * N for _ in range(N)]

r, c = 0, -1
num = 1
dir = 0
while num <= N * N:
    r, c = r + dr[dir], c + dc[dir]
    if 0 <= r < N and 0 <= c < N and arr[r][c] == 0:
        arr[r][c] = num
        num += 1
    else:
        r, c = r - dr[dir], c - dc[dir]
        dir = (dir + 1) % 4


for line in arr:
    print(*line)
