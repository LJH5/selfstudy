import sys
sys.stdin = open('4835.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    int_list = list(map(int, input().split()))
    # 비교하기

    # 처음 m개의 합
    three_sum = 0
    for i in range(m):
        three_sum += int_list[i]

    # 처음 합을 최대, 최소로
    max_sum = three_sum
    min_sum = three_sum

    # 한칸씩 이동하면서 구하기
    for i in range(m, n):
        three_sum = three_sum - int_list[i-m] + int_list[i]
        if three_sum > max_sum:
            max_sum = three_sum
        if three_sum < min_sum:
            min_sum = three_sum

    print(f'#{tc} {max_sum - min_sum}')