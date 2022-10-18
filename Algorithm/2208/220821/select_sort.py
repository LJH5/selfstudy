# 삽입 정렬
a_list = [4, 5, 3, 1, 2]
for i in range(len(a_list) - 1):                                # 비교 횟수는 n-1 ~ 1 (n은 리스트의 길이)
    min_idx = i                                                 # 최소값의 index
    for j in range(i+1, len(a_list)):                           # 자신 다음 index부터 비교 i+1 ~ n
        if a_list[j] < a_list[min_idx]:                         # 자신보다 작으면
            min_idx = j                                         # 최소값의 index 갱신
    a_list[i], a_list[min_idx] = a_list[min_idx], a_list[i]     # 최소값과 나의 자리를 바꾸기

print(a_list)