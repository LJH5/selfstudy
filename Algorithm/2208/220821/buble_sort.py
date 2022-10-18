# 버블 정렬
# 리스트에서 인접한 두개의 요소를 비교하여 정렬
# 첫번째 실행에서 n-1번 비교 후 제일 큰 수 오른쪽으로 정렬됨
# 실행횟수는 1씩 줄어듬(하나씩 정렬되기 때문)
a_list = [4, 5, 3, 1, 2]

for i in range(len(a_list)-1, 0, -1):
    for j in range(i):
        if a_list[j] > a_list[j+1]:
            a_list[j], a_list[j+1] = a_list[j+1], a_list[j]

print(a_list)