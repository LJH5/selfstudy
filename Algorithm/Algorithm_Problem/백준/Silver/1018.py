# 체스판 다시 칠하기
# 8 x 8 체스판을 만들 때
# 다시 칠하는 횟수가 가장 적을 때는 몇번 인가


N, M = map(int, input().split())
board = list(input() for _ in range(N))

pattern_a = 'BWBWBWBWBW'
pattern_b = 'WBWBWBWBWB'

for r in range(N-7):
    for c in range(M-7):
        print(r, c)
# B로 시작
# W로 시작