# # 길이 5이고 모든 요소가 0인 일차원 리스트
# a = [0 for i in range(5)]
# print(a)
# # 행렬이 5이고 모든 요소가 0인 일차원 리스트
# b = [[0 for i in range(5)]for j in range(5)]
# print(b)

lst = []
for i in range(2):
    lst.append(list(map(int, input().split())))
print(lst)

n = 5
m = 2
# lst = []
# for i in range(n):
#     lst.append(list(map(int, input().split())))
# print(lst)

lst = [
[1, 3,  3,  6,  7],
[8, 13, 9,  12, 8],
[4, 16, 11, 12, 6],
[2, 4,  1,  23, 2],
[9, 13, 4,  7,  3]
]

#가장 큰 수부터 찾는다

#2차원 리스트의 max는 코드이 첫번째 값만 비교
# print(max(lst))
