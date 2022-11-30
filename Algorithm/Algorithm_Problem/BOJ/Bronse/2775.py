# k층 n호에 살려면
# (k-1)층의 1~n호까지 사람들의 수를 합친만큼 살아야함
# n호에는 n명이 살고있음
#
import sys
input = sys.stdin.readline


def check(k, n):
    # print(f'Test case: {tc+1}')
    floor = list(i for i in range(1, n + 1))
    # print(f'0층: {floor}')
    for i in range(1, k+1):
        floor = nextFloor(floor)
        # print(f'{i}층: {floor}')

    return floor[n-1]


def nextFloor(floor):
    for i in range(1, len(floor)):
        floor[i] += floor[i-1]      # 누적합을 계산
    return floor


for tc in range(int(input())):
    result = check(int(input()), int(input()))
    print(result)

'''
n이 1이면 1
n이 2이면 k+2
n이 3이면 

1 5 14
1 4 10
1 3 6 10 15
1 2 3 4 5 6 7 8 9 10 11 12 13 14
'''
