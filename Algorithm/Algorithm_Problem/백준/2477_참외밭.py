# 참외밭은 항상 ㄱ 모양으로 주어짐
# 참외는 1m^2 당 melon개가 있다
# 방향이 주어짐 -> 1: 동쪽, 2: 서쪽, 3: 남쪽, 4, 북쪽
# 임의의 꼭지점에서 무조건 반시계방향

# 경우의 수는 4가지가 있다
# 동북동북 1414
# 북동북동 4141
# 동남동남 1313
# 남서남서 3232

melon = int(input())
direct_arr = []             # 방향의 순서를 저장
length_arr = []             # 방향의 거리를 저장
count = [0, 0, 0, 0, 0]     # 동, 서, 남, 북 개수를 저장
for i in range(6):
    direct, length = map(int, input().split())
    direct_arr.append(direct)
    length_arr.append(length)
    count[direct] += 1

# 최대 크기는 1개만 있는 것들을 곱한다
max_field = 1
one_arr = []
for i in range(1, 5):
    if count[i] == 1:
        one_arr.append(i)
for i in range(6):
    if direct_arr[i] in one_arr:
        max_field *= length_arr[i]

# 배열을 두배로 만들어 준다
tmp_arr = direct_arr[:]
tmp_arr *= 2
min_list = []
for i in range(9):
    if tmp_arr[i:i+2] == tmp_arr[i+2:i+4]:
        min_list = [i+1, i+2]
        break
min_field = length_arr[min_list[0]]*length_arr[min_list[1]]
print((max_field - min_field)*melon)