# import sys
# input = lambda: sys.stdin.readline().rstrip('\r\n')
#
# n = int(input())
# time_list = [tuple(map(int, input().split())) for _ in range(n)]
# time_list = sorted(time_list, key=lambda x: (x[0], x[1]))    # 정렬하기
# # 시작 시간이 같을때 짧은 거만 남기고 긴거는 삭제해도 될듯?
a = [(1, 2), (1, 1)]
print(set(a))