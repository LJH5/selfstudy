N = 7
arr = [[0] * N for _ in range(N)]
r, c = 2, 2
arr[r][c] = '*'

# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 대각선
# dr = [-1, -1, 1, 1]
# dc = [-1, 1, 1, -1]

# 기본적인 사방탐색
# for k in range(4):
#     nr = r + dr[k]
#     nc = c + dc[k]
#     arr[nr][nc] = k + 1

# 기준점 포함: 0부터, 기준점 포함 안 함: 1부터
# for i in range(1, 3):
#     nr = r + dr[1]*i
#     nc = c + dc[1]*i
#     arr[nr][nc] = 1

# 배열 끝까지 사방탐색
# for k in range(4):
#     for i in range(1, N):
#         nr = r + dr[k]*i
#         nc = c + dc[k]*i
#         if not(0 <= nr < N and 0 <= nc < N):
#             continue
#         arr[nr][nc] = k + 1

# for _ in range(1, N):
#     nr, nc = r + dr[1], c + dc[1]
#     if not (0 <= nr < N and 0 <= nc < N):
#         break
#     arr[nr][nc] = 1

while 0 <= r + dr[1] < N and 0 <= c + dc[1] < N:
    nr, nc = r + dr[1], c + dc[1]
    arr[nr][nc] = 1

for line in arr:
    print(*line)