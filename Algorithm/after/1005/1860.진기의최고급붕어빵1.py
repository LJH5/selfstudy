import sys; sys.stdin = open('1860.txt')

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())         # 손님수, 생성시간, 개수
    times = list(map(int, input().split()))     # 정렬된 상태가 아님
    times.sort()

    total = 0                               # 붕어빵의 현재 개수
    ans = 'Possible'
    for i in range(N):
        if (times[i]//M)*K  < i + 1:        # 시간 t에 가능한 붕어빵수  (t // M) * K
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')
