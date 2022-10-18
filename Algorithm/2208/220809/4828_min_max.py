T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #숫자 입력 받기
    n = int(input())
    num_list = list(map(int, input().split()))

    max_index = 0
    min_index = 0

    for i in range(n):
        if num_list[max_index] < num_list[i]:
            max_index = i
        if num_list[min_index] > num_list[i]:
            min_index = i

    print(f'#{test_case} {num_list[max_index] - num_list[min_index]}')
