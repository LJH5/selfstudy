import sys
sys.stdin = open('input.txt', 'r')
# 시간이 주어지는데 안겹치는 시간을 중 가장 많은 거
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time_list = []
    for i in range(N):
        start, end = map(int, input().split())
        time_list.append((start, end))
    
    time_list.sort(key=lambda x: x[1])
    check = time_list.pop(0)
    cnt = 1
    while time_list:
        if time_list[0][0] < check[1]:
            time_list.pop(0)
        else:
            check = time_list.pop(0)
            cnt += 1
            
    print(f'#{tc} {cnt}')