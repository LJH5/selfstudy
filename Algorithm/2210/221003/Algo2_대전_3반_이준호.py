# 보석의 종류는 5가지: 4, 6, 7, 9, 11
# 각 보석은 보석의 배수에 해당하는 가치를 가질 수 있다, 4번 보석과 8번 보석은 같은 종류
# 예산에 맞게 보석을 최대 가치로 사야한다
# N은 보석의 총 개수, M은 예산
# 부분집합으로 해결?

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    jem_list = list(map(int, input().split()))
    want_jem = []   # 수집 대상을 저장할 리스트
    result = 0
    for jem in jem_list:
        if jem % 4 == 0:
            want_jem.append(jem)
        elif jem % 6 == 0:
            want_jem.append(jem)
        elif jem % 7 == 0:
            want_jem.append(jem)
        elif jem % 9 == 0:
            want_jem.append(jem)
        elif jem % 11 == 0:
            want_jem.append(jem)

    # 부분 집합을 구한다
    for i in range(1 << len(want_jem)):
        tmp = []
        for j in range(len(want_jem)):
            if i & (1 << j):
                tmp.append(want_jem[j])
        if result < sum(tmp) <= M:
            result = sum(tmp)

    print(f'#{tc} {result}')