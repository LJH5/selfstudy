import sys
input = sys.stdin.readline

n = int(input())

nums = list(int(input()) for _ in range(n))

for num in sorted(nums):
    print(num)