T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N 입력 받기 -> 사각형 한 변의 길이
    N = int(input())
    # N x N 행렬 만들기 초기값 0으로
    snail_list = [[0]*N for _ in range(N)]

    num = 1             # 1부터 순서대로 올라갈 변수
    start_num = 0       # 사각형 시작 숫자
    max_num = N*N       # 마지막 숫자
    end_index = 0       # 마지막 인덱스 번호

    while N > 0:
        end_index = start_num + N - 1

        # N이 홀수이면 중앙에 한칸이 남는 경우를 처리
        if start_num == end_index:
            snail_list[start_num][end_index] = num

        # 첫번째: i start_num 고정, j는 start_num 부터 end_index 전까지 이동
        for j in range(start_num, end_index):
            if snail_list[start_num][j] == 0:
                snail_list[start_num][j] = num
                num += 1

        # 두번째: j는 end_index 고정, i는 start_num 부터 end_index 전까지 이동
        for i in range(start_num, end_index):
            if snail_list[i][end_index] == 0:
                snail_list[i][end_index] = num
                num += 1

        # 세번째: i는 end_index 고정, j는 end_index 부터 start_num 전까지 이동
        for j in range(end_index, start_num, -1):
            if snail_list[end_index][j] == 0:
                snail_list[end_index][j] = num
                num += 1


        # 네번째: j는 start_num 고정, i는 end_index 부터 start_num 전까지 이동
        for i in range(end_index, start_num, -1):
            if snail_list[i][start_num] == 0:
                snail_list[i][start_num] = num
                num += 1

        # 작은 사각형으로 생각
        N -= 2
        # 시작 숫자 +1
        start_num += 1

    # 결과 출력
    print(f'#{test_case}')
    for i in snail_list:
        for j in i:
            print(j, end=' ')
        print()