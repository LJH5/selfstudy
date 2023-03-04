from collections import deque
def check_bingo():
    bingo = 0
    # 가로 빙고
    for i in range(5):
        if sum(bingo_matrix[i]) == 0:
            bingo += 1
            if bingo >= 3:
                return bingo
    # 세로 빙고
    for i in range(5):
        for j in range(5):
            if bingo_matrix[j][i] != 0:
                break
        else:
            bingo += 1
            if bingo >= 3:
                return bingo
    # 대각선 빙고
    for i in range(5):
        if bingo_matrix[i][i] != 0:
            break
    else:
        bingo += 1
        if bingo >= 3:
            return bingo

    for i in range(5):
        if bingo_matrix[i][4-i] != 0:
            break
    else:
        bingo += 1
        if bingo >= 3:
            return bingo

    return bingo

bingo_matrix = [list(map(int, input().split())) for _ in range(5)]
mc_q = deque()
for _ in range(5):  # mc가 부르는 숫자 queue로 저장
    mc_q.extend(map(int, input().split()))

while mc_q:
    flag = False
    n = mc_q.popleft()
    for i in range(5):
        for j in range(5):
            if bingo_matrix[i][j] == n:
                bingo_matrix[i][j] = 0
            else:
                continue

    # 빙고 확인
    if check_bingo() >= 3:
        print(25 - len(mc_q))
        break