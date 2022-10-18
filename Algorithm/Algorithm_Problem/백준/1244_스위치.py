# 남학생은 자기 번호의 배수의 스위치 상태를 바꾼다 -> 인덱스
def boy(num):
    idx = num - 1
    for i in range(idx, len(switch_arr), num):  # 입력 받은 숫자부터 배수로
        if switch_arr[i]:  # 1일때
            switch_arr[i] = 0  # 0으로
        else:  # 0일때
            switch_arr[i] = 1  # 1로


# 여학생은 자기 번호를 중심으로 최대 좌우 대칭의 스위치 상태를 바꾼다(항상 홀수개)
def girl(num):
    idx = num - 1
    for i in range(n):  # idx를 중심으로 좌우가 대칭인지 확인
        if idx - i >= 0 and idx + i < n and switch_arr[idx - i] == switch_arr[idx + i]:
            if switch_arr[idx - i]:      # 1일때
                switch_arr[idx - i] = 0  # 0으로
                switch_arr[idx + i] = 0
            else:                        # 0일때
                switch_arr[idx - i] = 1  # 1로
                switch_arr[idx + i] = 1
        else:
            break

n = int(input())                                # n개의 스위치
switch_arr = list(map(int, input().split()))    # 스위치의 상태는 입력 받음
people = int(input())
for i in range(people):
    gen, data = map(int, input().split())
    if gen == 1:    # 남학생
        boy(data)
    else:           # 여학생
        girl(data)

for i in range(0, len(switch_arr), 20):
    print(*switch_arr[i:i+20])
