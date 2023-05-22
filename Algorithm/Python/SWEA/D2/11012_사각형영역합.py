# 사각영역들의 합
# N*N의 영역, 정사각형 M개
# 좌상단의 좌표, 한변의 길이
# 사각형 영역의 합을 구하라(겹치는 부분은 중복 계산 x)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = set()
    result = 0
    for _ in range(M):                                  # 정사각형의 개수만큼 입력 받음
        r, c, w = map(int, input().split())             # r, c는 좌상단의 좌표, w는 한변의 길이
        for i in range(r, r + w):                       # 사각형의 높이의 좌표는 r ~ r+w-1
            for j in range(c, c + w):                   # 사각형의 너비의 좌표는 c ~ c+w-1
                if 0 <= i < N and 0 <= j < N:           # 사각형이 배열의 영역안에 있으면서
                    if (i, j) not in visited:           # 이미 계산한 값이 아니라면
                        visited.add((i, j))             # 계산한 값으로 확인
                        result += matrix[i][j]          # 값을 더해준다
    print(f'#{tc} {result}')
