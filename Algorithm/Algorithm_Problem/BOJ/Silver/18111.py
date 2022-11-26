# 마인크래프트
# N: 세로, M: 가로, B: 인벤토리에 블럭 개수
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
matrix = list(map(int, input()) for _ in range(N))

print(matrix)