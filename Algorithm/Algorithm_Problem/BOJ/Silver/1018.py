# 체스판 다시 칠하기
# 8 x 8 체스판을 만들 때
# 다시 칠하는 횟수가 가장 적을 때는 몇번 인가


N, M = map(int, input().split())
board = list(input() for _ in range(N))
size = 8
odd_B_pattern = 'BWBWBWBW'
even_B_pattern = 'WBWBWBWB'

result = 9999

for r in range(N-size+1):                               # 가로먼저 정해주고
    for c in range(M-size+1):                           # 세로를 정해주고
        B_pattern_cnt = 0                               # 처음을 B로 시작하는 패턴
        W_pattern_cnt = 0                               # 처음을 W로 시작하는 패턴
        for line in range(r, r + 8):                    # 보드를 가져오고
            target = board[line][c:c + 8]               # 8개로 자르고
            for i in range(size):                       # 각 패턴과 비교
                if line % 2:                            # 홀수라인 일 때
                    if odd_B_pattern[i] != target[i]:   # 패턴과 일치하지 않으면
                        B_pattern_cnt += 1              # B 패턴 칠하는 수 +1
                    else:                               # 일치하면
                        W_pattern_cnt += 1              # W 패턴 칠하는 수 +1
                else:
                    if even_B_pattern[i] != target[i]:  # 일치하지 않으면
                        B_pattern_cnt += 1              # B 패턴 칠하는 수 +1
                    else:                               # 일치하면
                        W_pattern_cnt += 1              # W 패턴 칠하는 수 +1
            if B_pattern_cnt >= result and W_pattern_cnt >= result:     # 백 트래킹 이미 초과하면 종료
                break
        if result > min(B_pattern_cnt, W_pattern_cnt):  # 두 패턴을 칠하는 횟수 중 작은 것이 결과값보다 작으면
            result = min(B_pattern_cnt, W_pattern_cnt)  # 결과값 최소값으로 갱신

print(result)