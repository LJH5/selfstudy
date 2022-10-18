# # for문 순열 3C3
# arr = [1, 2, 3]
# # 순열
# print('순열')
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         for k in range(len(arr)):
#             if i != j and j != k and k != i:
#                 print(arr[i], arr[j], arr[k])
#
# # 중복 순열
# sel = [0]*3
# def rep_perm(depth):
#     if depth == 3:
#         print(*sel)
#         return
#
#     for i in range(len(arr)):
#         sel[depth] = arr[i]
#         rep_perm(depth+1)
# print('중복 순열')
# rep_perm(0)
#
# # 재귀 순열
# check = [0]*3
# def perm(depth):
#     if depth == 3:
#         print(*sel)
#         return
#
#     for i in range(len(arr)):
#         if not check[i]:
#             check[i] = 1
#             sel[depth] = arr[i]
#             perm(depth+1)
#             check[i] = 0
# print('재귀 순열')
# perm(0)
