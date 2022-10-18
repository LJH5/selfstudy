# 평균을 구해서 각 영역의 평균과의 차이를 더하는 것
# 입력

T = int(input())                # tc
for tc in range(1, T+1):
    result = 0
    n = int(input())                            # 영역의 크기 nxn
    pointer = list(map(int, input().split()))   # 평탄화 영역

    matrix = [list(map(int, input().split())) for _ in range(n)]    # 전체 영역
    # 평탄화할 영역 구하기
    start_y, start_x = pointer[0], pointer[1]
    end_y, end_x = pointer[2], pointer[3]
    total_sum = 0                               # 영역의 총합
    cnt = 0                                     # 영역의 개수

    for y in range(start_y, end_y+1):           # 정해진 영역을
        for x in range(start_x, end_x+1):       # 순환하여
            total_sum += matrix[y][x]           # 영역의 총합과
            cnt += 1                            # 영역의 개수를 구한다

    avg = total_sum//cnt                        # 평균을 구한다

    for y in range(start_y, end_y+1):
        for x in range(start_x, end_x+1):
            if matrix[y][x] - avg < 0:           # 평균보다 작을때
                result += avg - matrix[y][x]
            else:                                # 평균보다 클때
                result += matrix[y][x] - avg

    print(f'#{tc} {result}')