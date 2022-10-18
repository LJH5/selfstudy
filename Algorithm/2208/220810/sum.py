import sys
sys.stdin = open('sum.txt', 'r')

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    number_list = [list(map(int,input().split()))for _ in range(100)]
    max_value = 0
    tmp_sum = 0

    # 행의 합
    for i in range(100):
        tmp_sum = 0
        for j in range(100):
            tmp_sum += number_list[i][j]
        if tmp_sum > max_value:
            max_value = tmp_sum

    # 열의 합
    tmp_sum = 0
    for i in range(100):
        tmp_sum = 0
        for j in range(100):
            tmp_sum += number_list[j][i]
        if tmp_sum > max_value:
            max_value = tmp_sum

    # 대각선1의 합
    tmp_sum = 0
    for i in range(100):
        tmp_sum += number_list[i][i]
    if tmp_sum > max_value:
        max_value = tmp_sum

    # 대각선2의 합
    tmp_sum = 0
    for i in range(100):
        tmp_sum += number_list[i][99-i]
    if tmp_sum > max_value:
        max_value = tmp_sum

    print(f'#{test_case} {max_value}')