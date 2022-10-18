import sys; sys.stdin = open('1860.txt')

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())         # 손님수, 생성시간, 개수
    times = list(map(int, input().split()))     # 정렬된 상태가 아님
    times.sort()                                # 도착순으로 정렬

    total = 0                               # 붕어빵의 현재 개수
    ans = 'Possible'
    for t in range(0, 11111 + 1):
        if t != 0 and t % M == 0:                      # M초마다 K개 더하기
            total += K
        # t초에 손님이 도착하는지 확인
        if t in times:
            if total <= 0:
                # impossible 기록
                ans = 'Impossible'
                break
            else:
                total -= 1          # 손님에게 제공

    print(f'#{tc} {ans}')