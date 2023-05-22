from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

n, m = map(int, input().split())
memo = defaultdict(str)

for i in range(n):
    url, password = input().split()
    memo[url] = password

for j in range(m):
    url = input()
    print(memo[url])