# 비용을 나타내는 2차원 배열이 있을때
# +로 피는 꽃을 겹치는 부분이 없이 심을 때
# 최소비용을 구하여라
# 씨앗은 총 3개
import sys
field = [list(map(int, sys.stdin.readline().split())) for _ in range(int(input()))]  # 이게 되는구나... 뒤에 input이 먼저 실행되는 구나

