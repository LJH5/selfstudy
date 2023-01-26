from collections import deque
# 1 ~ 5번째 줄은 내 빙고판
# 최소한 빙고가 나오려면 13개 부터
# 대각선 숫자일때만 대각선 판단(역 대각선도 마찬가지)

# 그 인덱스의 가로 세로 빙고 찾기
def check_xy(i, j):
    global bingo
    # 가로 찾기
    if bingo_matrix[i].count('b') == 5:
        bingo += 1

    # 세로 찾기
    for k in range(5):
        if bingo_matrix[k][j] != 'b':
            break
    else:
        bingo += 1

# 대각 찾기
def check_dia():
    global bingo
    # 대각선 찾기
    for i in range(5):
        if bingo_matrix[i][i] != 'b':
            break
    else:
        bingo += 1

# 역대각선 찾기
def check_revdia():
    global bingo
    for i in range(5):
        if bingo_matrix[i][4-i] != 'b':
            break
    else:
        bingo += 1

bingo_matrix = [list(map(int, input().split())) for _ in range(5)]

mc_queue = deque()
for _ in range(5):  # mc가 부르는 숫자 queue로 저장
    mc_queue.extend(map(int, input().split()))

# 빙고 숫자 확인
bingo = 0
while mc_queue:
    n = mc_queue.popleft()               # 숫자 하나를 부름
    for i in range(5):
        for j in range(5):
            if bingo_matrix[i][j] == n:
                bingo_matrix[i][j] = 'b'
                if i == j:               # 대각선 숫자이면 다 확인
                    check_xy(i, j)
                    check_dia()
                elif i+j == 4:           # 역대각선
                    check_xy(i, j)
                    check_revdia()
                else:                    # 아니면 가로 세로만 확인
                    check_xy(i, j)
                break
    if bingo >= 3:                       # 빙고가 3줄이라면 빙고
        print(25 - len(mc_queue))    # 몇번째 수를 불렀을 때 빙고인지
        break