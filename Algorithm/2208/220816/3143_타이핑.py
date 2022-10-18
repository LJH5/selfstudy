# 입력
# 단어 수
# 단어 (반복)
T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    poham_cnt = A.count(B)
    # A의 총 글자 수 - (B의 글자 수 - 1)*B의 개수
    result = len(A) - (len(B) - 1)*poham_cnt
    print(f'#{tc} {result}')