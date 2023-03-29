import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

n = int(input())
time_list = [tuple(map(int, input().split())) for _ in range(n)]
time_list = sorted(time_list, key=lambda x: (x[0], x[1]))    # 정렬하기

for i in range(n):
    start_time, end_time = time_list[i]
    for j in range(n - i):