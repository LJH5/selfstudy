for _ in range(int(input())):
    dp = [(1, 0), (0, 1)]
    n = int(input())
    if n < 2:
        print(*dp[n])
    else:
        for i in range(2, n+1):
            dp.append((dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]))
        print(*dp[n])