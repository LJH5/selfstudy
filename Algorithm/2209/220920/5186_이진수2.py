# 주어진 값에 각 자리수를 뺄때
# 0이상 이면 빼고 작으면 그대로 둔다
# 이때 주어진 값이 0이 되면 종료
# 소수점 자리만 출력
# 13자리까지 간다면 overflow 출력
T = int(input())
for tc in range(1, T+1):
    result = 0
    N = float(input())
    result = 'overflow'
    cnt = -1
    bin = ''
    
    for _ in range(13):                 # 13자리 이상은 overflow 출력
        if N - 2**(cnt) >= 0:           # 2진수로 바꿈
            bin += '1'                  # 2진수로 바꿀 시 해당하는 자릿수
            N = N - 2**(cnt)            # 나머지 값
            if N == 0:                  # 2진수로 바뀜
                result = bin
                break
        else:
            bin += '0'                  # 2진수로 바꿀 시 해당하는 자릿수
        cnt -= 1                        # 다음 자릿수로 이동

    print(f'#{tc} {result}')
