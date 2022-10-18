# 별 4 > 동그라미 3 > 네모 2 > 세모 1
# 입력
# tc
# a 4개 3 4 2 1
# b 5개 4 2 3 1 2
T = int(input())
for tc in range(1, T+1):
    result = ''
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 0번째 인덱스 개수, 1번부터 딱지
    a_cnt = [0]*5
    b_cnt = [0]*5
    for i in range(1, len(a)):          # 인덱스를 이용해 개수를 저장
        a_cnt[a[i]] += 1
    for i in range(1, len(b)):
        b_cnt[b[i]] += 1
    if a_cnt == b_cnt:                  # 같으면 결과는 D
        result = 'D'
    else:
        for i in range(4, 0, -1):
            if a_cnt[i] > b_cnt[i]:     # 4의 개수부터 비교
                result = 'A'
                break
            elif a_cnt[i] < b_cnt[i]:
                result = 'B'
                break

    print(result)