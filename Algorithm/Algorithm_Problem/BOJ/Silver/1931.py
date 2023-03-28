import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

n = int(input())
time_list = [tuple(map(int, input().split())) for _ in range(n)]

print(sorted(time_list, key = lambda x : (x[0], x[1])))
