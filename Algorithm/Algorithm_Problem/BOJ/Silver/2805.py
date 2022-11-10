# 나무 자르기
# 이진탐색
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2        # 중간
    total_h = 0                     # 잘린 나무 길이의 합

    for tree in trees:          
        if tree >= mid:             # 중간 길이보다 길면
            total_h += tree - mid   # 잘라버리기

    if total_h >= M:                # 잘린 나무 길이의 합이 원하는 길이 이상이면
        start = mid + 1             # 자르는 높이 1증가
    else:                           # 잘린 나무 길이의 합이 원하는 길이 보다 작으면
        end = mid - 1               # 자르는 높이 1감소

print(end)