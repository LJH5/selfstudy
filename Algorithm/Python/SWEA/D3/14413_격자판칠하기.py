# 배열의 인덱스를 합해보면
# 짝 홀 짝
# 홀 짝 홀
# 찍 홀 짝
# 다음과 같이 격자 모양으로 됨

def check(odd, even):
    for r in range(N):
        for c in range(M):
            if (r + c) % 2:                 # 인덱스의 합이 홀수인 경우
                if board[r][c] == even:     # 짝수 값과 같으면
                    return False            # 거짓
            else:                           # 인덱스의 합이 짝수인 경우
                if board[r][c] == odd:      # 홀수 값과 같으면
                    return False            # 거짓
    return True                             # 아니라면 참

for tc in range(int(input())):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    result = 'impossible'

    case1 = check('#', '.')     # 짝이 '#', 홀이 '.'인 경우
    case2 = check('.', '#')     # 짝이 '.', 홀이 '#'인 경우
    if case1 or case2:          # 둘중 하나라도 만족하면
        result = 'possible'

    print(f'#{tc+1} {result}')