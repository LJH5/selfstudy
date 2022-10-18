# N명의 신입사원은 A, B, C 중에 하나에 분반
# 한 반의 인원은 최소 K_MIN명 최대 K_MAX명이다
# 신입사원의 수는 최소인원 * 3 <= n < 최대인원 * 3
# 반배정이 불가능하면 -1
# 가장 많은 인원으로 구성된 분반과 가장 적은 인원으로 구성된 분반의 인원 수 차이값이
# 최소가 되는 경우를 찾아 그 값을 출력하는 프로그램을 작성하라.
# C < T1 <= B < T2 <= A
# 알트 + 쉬프트 드래그 하면 테스트 케이스만 드래그 가능
# 1             tc
# 6 1 4         N: 사원의 수, K_MIN: 최소 인원, K_MAX: 최대 인원
# 2 2 3 4 4 5   사원의 점수
T = int(input())
for test_case in range(1, T + 1):
    N, K_MIN, K_MAX = map(int, input().split())
    SCORE = [int(num) for num in input().split()]
    count = [0]*(max(SCORE)+1)
    result = 999
    for i in SCORE:
        count[i] += 1
    for T1 in range(1, len(count)):             # 인덱스는 0부터 시작
        for T2 in range(T1, len(count)):        # 최소 인원이 0인 경우도 포함
            C, B, A = 0, 0, 0
            for i in range(len(count)):
                if i < T1:
                    C += count[i]
                elif i < T2:
                    B += count[i]
                else:
                    A += count[i]
            if K_MIN <= C <= K_MAX and K_MIN <= B <= K_MAX and K_MIN <= A <= K_MAX:
                tmp = max(C, B, A) - min(C, B, A)
                if tmp < result:
                    result = tmp
    if result == 999:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {result}')