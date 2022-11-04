# ATM
import sys


def time_accumulate():      # 누적합을 계산하는 함수
    ac = 0                  # 누적합을 저장할 변수
    total_time = 0          # 총 걸린 시간을 저장할 변수
    for time in line:       # 처리시간을 하나씩 가지고 온다
        ac += time          # 누적합에다가 더하고
        total_time += ac    # 누적합을 총 걸린 시간에 더해준다
    return total_time       # 총 걸린 시간을 반환


n = int(input())
line = list(map(int, sys.stdin.readline().split()))

line.sort()                 # 처리 시간이 짧은 사람부터 처리하기위해 정렬
result = time_accumulate()
print(result)