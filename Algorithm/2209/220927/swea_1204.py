# 같으면 점수가 큰 것을 출력
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cnt = [0] * 101
    result = 0
    tmp = 0
    for i in list(map(int, input().split())):
        cnt[i] += 1
    for i in range(len(cnt)):
        if cnt[i] >= tmp:
            tmp = cnt[i]
            result = i

    print(f'#{tc} {result}')
