# 준서야 요즘 군대 편해~
# 물품의 수 N, 준서가 버티는 무게 K
# 물건의 무개 W, 물건의 가치 V
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
sum_value = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, input().split())
    sum_value[W] = V
