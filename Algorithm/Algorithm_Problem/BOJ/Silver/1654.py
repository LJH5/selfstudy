import sys
input = sys.stdin.readline


def binSearch(cable_list):              # 이진탐색
    start = 1                           # 시작
    end = max(cable_list)               # 끝
    result = 0                          # 최대길이를 저장할 변수
    while start <= end:                 
        mid = (start + end) // 2        # 중간 값
        cable_cnt = countCables(mid)    # 중간 값의 길이로 자른 랜선의 수
        if cable_cnt < n:               # 원하는 개수보다 모자라면
            end = mid - 1               # 짧게 자르기
        else:                           # 원하는 개수보다 많으면 
            if mid > result:            # 최대길이보다 크면 
                result = mid            # 최대길이 갱신
            start = mid + 1             # 길게 자르기

    return result                       # 최대길이를 리턴


def countCables(mid):                   # 중간 값으로 자른 랜선의 개수를 구하는 함수
    cnt = 0                             # 랜선의 개수
    for cable in cables:                # 랜선을 가지고 와서
        cnt += cable // mid             # 중간 값으로 자랐을 때 만들어지는 랜선의 개수를 누적합
    return cnt                          # 총 랜선의 개수 반환


k, n = map(int, input().split())
cables = list(int(input()) for _ in range(k))

print(binSearch(cables))