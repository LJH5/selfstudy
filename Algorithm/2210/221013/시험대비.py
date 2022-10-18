# n명의 신입사원은 A, B, C 중에 하나에 분반
# 한 반의 인원은 최소인원 ~ 최대인원
# 신입사원의 수는 최소인원 * 3 <= n < 최대인원 * 3
# 반배정이 불가능하면 -1
# 가장 많은 인원으로 구성된 분반과 가장 적은 인원으로 구성된 분반의 인원 수 차이값이
# 최소가 되는 경우를 찾아 그 값을 출력하는 프로그램을 작성하라.
# C < T1 <= B < T2 <= A
# set으로 중복제거를 하고 3개보다 많으면 result = -1

T = int(input())
for test_case in range(1, T + 1):
    N, K_MIN, K_MAX = map(int, input().split())
    SCORE = [int(num) for num in input().split()]
    count = [0]*(max(SCORE)+1)
    result = 999
    for i in SCORE:
        count[i] += 1
    print(count)
    arr = sorted(list(set(SCORE)))

    for i in range(len(arr)-1):
        T1 = arr[i]
        for j in range(i+1, len(arr)):
            A = []
            B = []
            C = []
            T2 = arr[j]
            for k in SCORE:
                if k >= T2:
                    A.append(k)
                elif k >= T1:
                    B.append(k)
                else:
                    C.append(k)
            print(T1, T2)
            print(C, B, A)
            if len(A) < K_MIN or len(B) < K_MIN or len(C) < K_MIN or len(A) > K_MAX or len(B) > K_MAX or len(C) > K_MAX:
                continue
            else:
                if result > max(len(A), len(B), len(C)) - min(len(A), len(B), len(C)):
                    result = max(len(A), len(B), len(C)) - min(len(A), len(B), len(C))
    if result == 999:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {result}')