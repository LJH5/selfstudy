# 10x10 이차원 배열
# 사각형 개수
# 2 2 / 4 4 / 1
# 좌상단 모서리 / 우하단 모서리 / 색
# 색 1은 빨강, 2는 파랑
# 빨강과 파랑이 겹쳐지는 칸 수를 구하여라
# 색칠된 10x10 테이블을 만드는 함수

import sys
sys.stdin = open('4837.txt', 'r')

def make_table(arr):
    # 현재위치는 좌상단 모서리 인덱스
    start_r = arr[0]
    start_c = arr[1]
    # 최대로 이동할 수 있는 곳 은 우하단 모서리 인덱스
    end_r = arr[2] + 1
    end_c = arr[3] + 1
    # 영역의 색
    color = arr[4]
    # 색칠하기
    for r in range(start_r, end_r):
        for c in range(start_c, end_c):
            # 빨강이면 빨간색 테이블에 색칠
            if color == 1:
                red_table[r][c] = 1
            # 파랑이면 파란색 테이블에 색칠
            else:
                blue_table[r][c] = 1

# 테스트 횟수
T = int(input())
for tc in range(1, T+1):
    # 비어있는 10x10 테이블 만들기
    red_table = [[0] * 10 for _ in range(10)]
    blue_table = [[0] * 10 for _ in range(10)]
    purple_cnt = 0

    # 영역의 개수 입력
    n = int(input())

    # 영역정보 입력 받기
    input_arr = [list(map(int, input().split())) for _ in range(n)]

    # 색 별로 테이블 색칠하기
    for i in range(n):
        make_table(input_arr[i])

    for i in range(10):
        for j in range(10):
            # 값이 1이고 (영역이 색칠되어 있고) 겹친 곳이라면
            if red_table[i][j] & blue_table[i][j]:
                purple_cnt += 1

    print(f'#{tc} {purple_cnt}')