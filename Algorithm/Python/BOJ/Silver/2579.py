import sys
input = sys.stdin.readline
n = int(input())
stairs = [0] + list(int(input()) for _ in range(n))
dp = [0] * (n+1)
dp[1] = stairs[1]
if n == 1:
   pass
else:
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, n+1):                             # n번째 칸은 무조건 밟아야 함
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i],  # n-1번째에서 한 칸 점프
                    dp[i-2] + stairs[i])                # n-2번째에서 두 칸 점프
    # print(stairs)
print(dp[n])