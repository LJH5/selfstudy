import sys
input = sys.stdin.readline

n = int(input())
members = list()
for _ in range(n):
    age, name = input().split()
    members.append([int(age), name])

members.sort(key=lambda x: x[0])

for member in members:
    print(*member)