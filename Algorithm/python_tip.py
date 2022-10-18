# # 리스트 순서 뒤집기
# a = [1, 2, 3, 4, 5]
# b = a[::-1]
# print(b)


# #문자열 자르기
# names = '아무개, 홍길동, 김첨지'
# name = names.split(',')
# print(name)

# # sort와 sorted
# # sort는 반환값 없음, sort는 반환값 있음
# a = [1, 5, 3, 4, 2]

# b = a.sort()  #b의 타입은 None, sort는 반환값이 없어서 다른 변수에 저장 불가능
# b = sorted(a) #b의 타입은 List, b에 정렬된 a리스트가 입력됨

# # 3*3 행렬 만들기
# mat = [[0]*3]*3
# mat[0][1] = 1
# # 결과값 [[0,1,0], [0,1,0], [0,1,0]]

# mat = [[0]*5 for _ in range(5)]
# mat[0][1] = 1
# # 결과값 [[0,1,0], [0,0,0], [0,0,0]]

# #[0]
# #[0,0]
# #[0,0,0] 만들기 
# mat = [[0]*x for x in range(1,3)]
    
# # 해당 문자열이 숫자인지 판별하기
# x = '3²'
# print(x.isdigit())  #해당 문자열이 '숫자'로 이루어져 있는지(단 '½' 같은 것은 False)
# # True
# print(x.isdecimal())    #해당 문자열이 int로 형변환이 되는 지(즉, 0~9사이의 숫자)
# # False
# print(x.isnumeric())    #해당 문자열이 '수로 볼 수 있는 것'인지('½' 같이 표현된 문자열도 True)
# # True
# int(x)
# # ERROR!!!!
aList = [[1, 2, 3], ['a', 'b', 'c']]

bList = [aList[i][0] for i in range(len(aList))]
print(bList)