# N: 손님의 수, M: 붕어빵 굽는 시간, K: 한 번 구을 때 붕어빵 개수
for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    result = 'Impossible'
    bbang = 0
    times = sorted(list(map(int, input().split())))
    for i in range(max(times)+1):   # 0 ~ 11111초
        if not i % M and i != 0:    # 0초는 제외해야함
            bbang += K
        if i in times:
            if bbang <= 0:
                break
            else:
                bbang -= 1
    else:
        result = 'Possible'
    print(f'#{tc} {result}')