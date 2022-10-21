n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
result = 0

a_list.sort()                       # a_list는 오름차순 정렬
b_list.sort(reverse=True)           # b_list는 내림차순 정렬
for i in range(n):
    result += a_list[i]*b_list[i]   # 두 리스트를 곱해서 더하면 최소값

print(result)