n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
dp[3] =
for i in range(4, 1001):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n] % 1007)