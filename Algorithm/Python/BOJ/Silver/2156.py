# 포도주 시식
# 3잔 연속으로 마실수 없다 2잔씩 마셔야함
import sys
input = sys.stdin.readline

N = int(input())
wine = [0] + list(int(input()) for _ in range(N))

dp = [0]*10001

for i in range(1, 3):
    dp[i] = dp[i-1] + wine[i]
    if N == 1:                  # 1 <= N <= 10000 1부터 올 수 있는 걸 주의하자
        break                   # 런타임만 3번 띄움

# 6 10 13 9 8 1 10
# 9를 기준으로 한다면
# 16 + 9        전전의 최대 와인량 + 현재 와인량
# 6 + 13 + 9    전전전의 쵀대 와인량 + 전의 와인량 + 현재 와인량
# 10 + 13       전의 최대 와인랭 (현재 와인은 마시지 않음)

for i in range(3, N+1):
    dp[i] = max(dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i], dp[i-1])

print(max(dp))