for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 999999
    for i in range(1, N-1):
        for j in range(i+1, N):
            tmp_sum = 0
            a, b, c = 0, 0, 0
            for x in range(N):
                if x < i:
                    a += arr[x]
                elif x < j:
                    b += arr[x]
                else:
                    c += arr[x]
            tmp_sum = max(a, b, c) - min(a, b, c)
            if tmp_sum < result:
                result = tmp_sum

    print(f'#{tc+1} {result}')