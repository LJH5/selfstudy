# 어디에 단어가 들어갈 수 있을까
def k_cnt(matrix):
    global cnt
    for i in range(len(matrix)):
        tmp_str = ''.join(matrix[i])              # 문자열로 만들고
        cnt += tmp_str.split('0').count('1' * k)  # '0'을 기준으로 나누어서 빈 공간이 k인 것 몇 개인지 세기

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())                    # n: 배열 크기, k: 크기 k의 단어
    matrix = [list(input().split())for _ in range(n)]   # matrix: n x n행렬, 문자열
    cnt = 0

    k_cnt(matrix)                       # 가로에 k 개수 더하기
    sero_matrix = list(zip(*matrix))    # 세로 리스트 만들기
    k_cnt(sero_matrix)                  # 세로에 k 개수 더하기

    print(f'#{tc} {cnt}')