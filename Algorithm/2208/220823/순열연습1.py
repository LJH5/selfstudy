arr = ['A', 'B', 'C', 'D']
sel = [0, 0]
check = [0, 0, 0, 0]

# 4개 중 2개를 골라서 출력
def perm(depth):
    if depth == 2:
        print(*sel)
        return
    for i in range(4):
        if not check[i]:
            check[i] = 1
            sel[depth] = arr[i]
            perm(depth + 1)
            check[i] = 0

perm(0)


# arr = ['A', 'B', 'C', 'D', 'E']
# sel = [0, 0, 0]
# check = [0, 0, 0, 0, 0]
# # 5개중 3개를 골라서 출력
# # 깊이는 3, 가지는 5개
#
# def perm(depth):
#     # 끝까지 간 경우 출력 후 종료
#     if depth == 3:
#         print(*sel)
#         return
#     for i in range(5):
#         if not check[i]:            # check가 0이면
#             check[i] = 1            # check에 1을 넣고
#             sel[depth] = arr[i]     # 해당하는 깊이에 배열의 값을 넣고
#             perm(depth+1)           # 다음 깊이로 넘어간다
#             check[i] = 0            # 끝까지 가고 출력후 돌아올 때 사용한 자리는 0으로 초기화 시킨다
#
# perm(0)