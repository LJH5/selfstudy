# 장훈이의 높은 선반
# 부분집합의 합이 선반의 높이와 차이가 가장 작은 것

def powerset(idx):
    global result
    if idx == N:                        # 부분집합 완성
        tmp = 0                         # 부분집합의 합을 저장할 임시 변수
        for i in range(N):
            if check[i] == 1:           # check가 1이면 선택된 요소
                tmp += tall_list[i]     # 합하기
        if 0 <= tmp - B < result:       # 선반 - 키의 합이 0 이상이여아하고, 최소값을 찾아야함
            result = tmp - B
        return

    for i in range(2):
        check[idx] = i
        powerset(idx + 1)

T = int(input())
for tc in range(1, T+1):
    result = 99999
    N, B = map(int, input().split())
    tall_list = list(map(int, input().split()))
    check = [0] * N
    powerset(0)
    print(f'#{tc} {result}')