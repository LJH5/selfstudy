import sys
input = sys.stdin.readline
n = int(input())
houses = [list(map(int, input().split())) for _ in range(n)]
# 1, 2번 집의 색은 달라야하고
# N, N-1번 집의 색은 달라야하고
# i-1, i, i+1번 집의 색은 달라야한다
# 0번째 줄은 처음 칠한 게 최소값
# 0을 빨강, 1을 파랑, 2를 초록으로 칠하는 비용이라고 하면
# 첫번째 집을 빨강으로 칠하면 2번째 집은 초록이나 파랑중에서 칠하면 됨
for i in range(1, n):
    houses[i][0] = min(houses[i - 1][1], houses[i - 1][2]) + houses[i][0]
    houses[i][1] = min(houses[i - 1][0], houses[i - 1][2]) + houses[i][1]
    houses[i][2] = min(houses[i - 1][0], houses[i - 1][1]) + houses[i][2]
print(houses)
print(min(houses[n - 1][0], houses[n - 1][1], houses[n - 1][2]))
