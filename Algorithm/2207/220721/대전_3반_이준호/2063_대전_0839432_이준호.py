# count개의 정수
count = int(input())
# 크기 count의 lsit 만들기
num_list =[0 for i in range(count)] 
# 정수 입력 받아 list에 넣기
num_list = list(map(int, input().split()))
if len(num_list) > count:
    print("입력 개수 초과")
    exit()
#num_list 오름차순 정렬
num_list.sort()
#중간값 구하기
mid_num = num_list[count//2]
#중간값 출력
print(mid_num)