T = int(input())
for tc in range(1, T+1):
    result = 0
    N, K = map(int, input().split())
    cnt = [0] * 1001
    for i in list(map(int, input().split())):
        cnt[i] = 1
    for i in range(len(cnt)):
        if cnt[i] == 1:
            K -= 1
            if K == 0:
                result = i
                break

    print(f'#{tc} {result}')