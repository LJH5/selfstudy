for tc in range(int(input())):
    N, M = map(int, input().split())
    flag = list(input() for _ in range(N))
    result = 999999999
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            cnt = 0
            for r in range(N):
                for c in range(M):
                    if r <= i:  # 흰줄
                        if flag[r][c] != 'W':
                            cnt += 1
                    elif r <= j:  # 파란줄
                        if flag[r][c] != 'B':
                            cnt += 1
                    else:  # 빨간줄
                        if flag[r][c] != 'R':
                            cnt += 1
            if cnt < result:
                result = cnt

    print(f'#{tc+1} {result}')