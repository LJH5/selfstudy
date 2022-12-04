import sys
input = sys.stdin.readline

for tc in range(int(input())):
    dp = [1, 2, 4]
    n = int(input())
    for i in range(3, n):
        tmp_sum = 0
        for j in range(1, 4):
            tmp_sum += dp[i-j]
        dp.append(tmp_sum)

    print(dp[n-1])