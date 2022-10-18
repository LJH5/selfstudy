original = input()
print('처음: ', original, type(original))
str_list = original.split()
print('아직 요소는 str: ', str_list, type(str_list[0]))
map_object = map(int, str_list)
print('처음 보는 친구인걸?: ', map_object)
list_flavour = list(map_object)
print('리스트 맛 젤리: ', list_flavour, type(list_flavour[0]))

nums = list(map(int, input().split))














# cover = 0
# for each_str in str_list:
#     str_list[cover] = int(each_str)
#     cover = cover + 1

# 왼쪽이 인덱스값, 오른쪽이 실제 보따리에서 나오는 값
# for cover, each_str in enumerate(str_list):
#     str_list[cover] = int(each_str)

# print(str_list, type(str_list[0]))