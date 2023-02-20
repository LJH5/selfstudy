import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

for i in range(m):
    s, e = map(int, input().split())
    print(sum(numbers[s-1:e]))