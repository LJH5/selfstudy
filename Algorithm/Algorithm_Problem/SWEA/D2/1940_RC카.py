# check가 0이면 유지, 1이면 가속, 2이면 감속 만약 감속이 더 크면 rc카의 속도는 0
T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())
    speed = 0
    for i in range(n):
        s = input()
        if int(s[0]) == 1:       # 가속이면
            speed += int(s[2])   # 현재속도(speed)+가속도(s[2])
        elif int(s[0]) == 2:     # 감속이면
            speed -= int(s[2])   # 현재속도(speed)-감속도(s[2])
            if speed < 0:        # 감속이 더 크면
                speed = 0        # rc카의 속도는 0
        result += speed          # 그순간 이동한 거리는 현재 속도(speed)
    print(f'#{tc} {result}')