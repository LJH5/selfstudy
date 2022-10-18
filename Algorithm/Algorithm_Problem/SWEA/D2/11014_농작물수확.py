import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    result = 9999999999
    N = int(input())
    farm = [list(map(int, input().split())) for _ in range(N)]
    for c in range(1, N-1):                             # c는 세로 자르기
        for r in range(1, N-1):                         # r은 가로 자르기
            field1, field2, field3 = 0, 0, 0            # 각 영역을 합을 저장할 변수
            for i in range(N):                          # 배열 다돌기
                for j in range(N):
                    if j >= c:                          # j가 세로로 자른 것 포함 오른쪽
                        field3 += farm[i][j]            # 영역3에 더하기
                    elif i < r:                         # j가 세로로 자른 것 제외 왼쪽, 가로로 자른 것 제외 위쪽
                        field1 += farm[i][j]            # 영역 1에 더하기
                    else:                               # j가 세로로 자른 것 제외 왼쪽, 가로로 자른 것 포함 아래쪽
                        field2 += farm[i][j]            # 영역 2에 더하기

            tmp = max(field1, field2, field3) - min(field1, field2, field3) # 최대값과 최소값의 차이
            if tmp < result:
                result = tmp

    print(f'#{tc} {result}')