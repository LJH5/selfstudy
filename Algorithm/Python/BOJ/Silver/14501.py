import sys
input = sys.stdin.readline

N = int(input())

task = []
dp = [0] * (N + 1)

for _ in range(N):
    day, value = map(int, input().split())
    task.append((day, value))

for i in range(N - 1, -1, -1):
    if task[i][0] + i > N:
        dp[i] = dp[i + 1]

    else:
        dp[i] = max(dp[i + 1], dp[task[i][0] + i] + task[i][1])

print(dp[0])