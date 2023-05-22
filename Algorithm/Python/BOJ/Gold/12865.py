# 준서야 요즘 군대 편해~
# 물품의 수 N, 준서가 버티는 무게 K
# 물건의 무개 W, 물건의 가치 V
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
item = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    item.append(list(map(int, input().split())))


for n in range(1, N + 1):           # n번째 물건
    for w in range(1, K + 1):       # 들 수 있는 무개
        weight = item[n][0]
        value = item[n][1]

        if w < weight:
            knapsack[n][w] = knapsack[n - 1][w]  # weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[n][w] = max(value + knapsack[n - 1][w - weight], knapsack[n - 1][w])

print(knapsack[N][K])