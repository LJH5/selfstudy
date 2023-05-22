def dfs(idx, depth):                                            # 모든 변경의 경우의 수 구하기
    global result
    if depth == cnt:                                            # 횟수 다 소진하면 종료
        if int(''.join(arr)) > result:                          # 최대 상금 구하기
            print(int(''.join(arr)))
            result = int(''.join(arr))
        return

    for i in range(idx, len(arr)):
        max_idx = i
        for j in range(i + 1, len(arr)):
            if arr[max_idx] <= arr[j]:                          # 작거나 같으면 바꾸기
                arr[max_idx], arr[j] = arr[j], arr[max_idx]     # 바꾼뒤에 넣어주기
                dfs(max_idx, depth + 1)
                arr[max_idx], arr[j] = arr[j], arr[max_idx]     # 다시 돌려주기

    if result == 0 and depth < cnt:                             # 만약 횟수 소모 전에 정렬된다면
        if (cnt - depth) % 2 and len(arr) == len(set(arr)):     # 그때 남은 횟수가 홀수이고 중복이 없으면
            arr[-1], arr[-2] = arr[-2], arr[-1]                 # 맨 뒤 2자리 바꾸기
        dfs(idx, cnt)                                           # depth에 cnt 넣고 재귀 종료시키기

T = int(input())
for tc in range(1, T+1):
    result = 0
    arr, cnt = input().split()
    arr = list(arr)
    cnt = int(cnt)
    dfs(0, 0)

    print(f'#{tc} {result}')

# 선택 정렬
# 최대값을 앞으로 보낸다
# 최대값이 동일하면 뒤에 있는 것을 보낸다
# T = int(input())
# for tc in range(1, T+1):
#     result = 0
#     arr, cnt = input().split()
#     arr = list(arr)
#     cnt = int(cnt)
#     sorted_arr = sorted(arr, reverse=True)              # 배열 내림차순
#     # 최대값을 찾은 뒤에 0번 인덱스에 삽입
#     i = 0
#     while cnt > 0:
#         max_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] >= arr[max_idx]:                      # 최대값의 인덱스 구하기
#                 max_idx = j
#         if arr[i] == arr[max_idx]:                          # 최대값이 자신아라면 자리 그대로
#             i += 1
#         else:
#             arr[i], arr[max_idx] = arr[max_idx], arr[i]     # 최대값과 자리를 바꿈
#             cnt -= 1                                        # 교환 횟수 1회 감소
#             i += 1
#         if sorted_arr == arr:                               # 배열이 이미 오름 차순 정렬이라면
#             break                                           # 정렬 종료
#     if cnt % 2 and len(arr) == len(set(arr)):               # 교환 횟수가 1회 남았고 중복되는 숫자가 없다면
#         arr[-1], arr[-2] = arr[2], arr[-1]                  # 마지막 두 자리를 바꿈
#     result = max(int(''.join(arr)), result)
#     print(f'#{tc} {result}')