# # for을 이용한 조합 5C2
# arr = [1, 2, 3, 4, 5]
# # 조합
# print('조합')
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         for k in range(j+1, len(arr)):
#             print(arr[i], arr[j], arr[k])
#
# # 중복조합
# print('중복 조합')
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         for k in range(j, len(arr)):
#             print(arr[i], arr[j], arr[k])
#
# # 재귀를 이용한 조합 5C3
# arr = [1, 2, 3, 4, 5]
# sel = [0]*3
# def combi(idx, sidx):
#     if sidx == len(sel):
#         print(*sel)
#         return
#
#     if idx == len(arr):
#         return
#
#     sel[sidx] = arr[idx]
#     combi(idx+1, sidx+1)
#     combi(idx+1, sidx)
#
# print('조합')
# combi(0, 0)
#
# def rep_combi(idx, sidx):
#     if sidx == len(sel):
#         print(*sel)
#         return
#
#     if idx == len(arr):
#         return
#
#     sel[sidx] = arr[idx]
#     rep_combi(idx, sidx+1)
#     rep_combi(idx+1, sidx)
#
# print('중복 조합')
# rep_combi(0, 0)