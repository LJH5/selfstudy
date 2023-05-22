# 1 1 1 2 2 3 4 5 7 9 12 16
# 0 1 2 3 4 5 6 7 8 9 10 11
# n 번째는 n-1번과 n-5번을 합친다
for _ in range(int(input())):
    dp = [0, 1, 1, 1, 2, 2]
    n = int(input())
    if n >= 6:
        for i in range(6, n+1):
            num = dp[i-1] + dp[i-5]
            dp.append(num)
    print(dp[n])
