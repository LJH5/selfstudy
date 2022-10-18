# for문 완전 정복하기
int_list = [1, 2, 3, 4, 5]
str_list = ['a', 'b', 'c', 'd', 'e']
dict_list = [{'name': '이준호', 'age': 28}, {'name': '홍길동', 'age': 30}, {'name': '아무개', 'age': 27}]

a_dict = {'name': '이준호', 'age': 28}

int_set = {1, 2, 3, 4, 5}
str_set = {'a', 'b', 'c', 'd', 'e'}

#range: 지정한 횟수만큼 반복
# for i in range(5):
#     print(i)

#list: list 안의 모든 값을 출력할 때까지 반복
# for i in int_list:
#     print(i)
# for i in str_list:
#     print(i)
# for i in dict_list:
#     print(i)

#dictionary: dictionary 안의 모든 키를 출력할 때까지 반복
# for key in a_dict:
#     print(key)
# dictionary 안의 모든 값을 출력할 때까지 반복
# for key in a_dict:
#     print(a_dict.get(key))
# dictionary 안의 모든 키-값 쌍을 출력할 때까지 반복
# for key, value in a_dict.items():
#     print(key, value)


#list comprehension
# lst = [i**2 for i in range(1,11) if i % 3 == 0] # 1~10까지의 숫자 중 3으로 나눈 나머지가 0인 i의 제곱 리스트 
# print(lst)
# lst = [dict_list[i].get('name') for i in range(len(dict_list))] # dict_list안의 모든 dictionary의 'name' key의 value를 리스트로 저장
# print(lst)