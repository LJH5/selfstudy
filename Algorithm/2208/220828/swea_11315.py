# N*N 바둑판
# .은 빈자리 o는 돌이 있음
# o가 5개 연속이면 YES/ 아니면 NO 출력
def check(arr):
    global result
    for i in range(n):
        if ''.join(arr[i])  == 'ooooo':
            return True
T = int(input())
for tc in range(1, T+1):
    result = 'NO'
    n = int(input())
    # 가로
    matrix = [list(input()) for _ in range(n)]
    if check(matrix):
        print(f'#{tc} YES')
        break
    # 세로
    sero_arr = list(zip(*matrix))
    if check(sero_arr):
        print(f'#{tc} YES')
        break
    # 대각선
