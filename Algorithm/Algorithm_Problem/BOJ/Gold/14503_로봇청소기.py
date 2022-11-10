import sys
sys.stdin = open('../input.txt')
# 청소하는 영역의 개수를 구하라?
# 빈칸은 0, 벽은 1
# r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수
# d는 청소기의 방향 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
# 현재위치를 청소
# 현재 방향을 기준으로 왼쪽부터 탐색 왼-앞-오-뒤
# 왼쪽 방향에 청소할 공간이 있으면 그 방향으로 회전하고 한칸 전진
# 현재위치를 청소
# 왼쪽 방향에 청소할 공간이 없으면 그 방향으로 회전하고
# 현재 방향을 기준으로 왼쪽부터 탐색 왼-앞-오-뒤
# 일단은 현재위치에서 왼쪽부터 봐야하니 사방탐색을 한다
N, M = map(int, input().split())
r, c, d = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(N)]
# 북 동 남 서 일때
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# 처음
matrix[r][c] = 2
result = 1
while True:
    for _ in range(4):
        # 청소 가능 구역이라면
        if matrix[r + dr[(d + 3) % 4]][c + dc[(d + 3) % 4]] == 0:
            # 방향 갱신
            d = (d + 3) % 4
            # 이동
            r += dr[d]
            c += dc[d]
            # 청소
            matrix[r][c] = 2
            result += 1
            break
        # 청소 구역이 아니라면 돌아라
        else:
            d = (d + 3) % 4
    else:
        r -= dr[d]
        c -= dc[d]
        if matrix[r][c] == 1:
            break
print(result)