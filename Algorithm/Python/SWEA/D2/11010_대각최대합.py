import sys
sys.stdin = open('input.txt')


def rotate():                           # 배열을 순회
    result = 0                          # 최대합을 저장할 변수
    for i in range(N):                  # 배열의 모든 위치를 순회
        for j in range(N):
            if cross(i, j) > result:    # 특정 좌표와 대각선의 합이 저장된 최대합보다 크면
                result = cross(i, j)    # 최대합 갱신

    return result

def cross(r, c):                    # 특정 좌표의 대각선의 합을 구함
    tmp_sum = matrix[r][c]          # 특정 좌표와 대각선 합을 저장하는 변수
    for k in range(4):              # 대각선 탐색
        for i in range(1, N):       # 대각선은 끝까지 감
            nr = r + dr[k]*i
            nc = c + dc[k]*i
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            tmp_sum += matrix[nr][nc]

    return tmp_sum

for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 대각선
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]


    print(f'#{tc+1} {rotate()}')