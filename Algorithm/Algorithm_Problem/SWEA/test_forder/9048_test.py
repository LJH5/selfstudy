# input
# 10
# cozy
# lummox
# gives
# smart
# squid
# who
# asks
# for
# job
# pen

# 1. 인풋에 모든 소문자가 들어있는지 확인
# ㄴ모든 인풋을 list로 저장해서 a~z까지 있는지 확인
# ㄴ for i in range(97, 123) => chr() 아스키코드
# n = int(input('입력 갯수: '))
# array = [[0] for i in range(n)]
# array[0][1] = 10
# print(array)
# for i in range(n):
#     pass
# for i in range(97, 123):
#     print(chr(i))




# 답 1
# ------------------------
# 6
# abcdefghi
# jklmnopqr
# stuvwxyz
# zyxwvuts
# rqponmlkj
# ihgfedcba

# ((1, 2, 3), 4, 5, 6)
# ((1, 2, 4), 3, 5, 6)
# ((1, 2,))

# array = []
# for i in range(3):
#     n = input()
#     array.append(list(n))
# print(array)
array = [['p', 'y', 't', 'h', 'o', 'n'], ['c', 'u', 't', 't', 'i', 'n', 'g'], ['m', 'a', 's', 't', 'e', 'r']]

for i in array:
    if 'a' in i:
        print(i)