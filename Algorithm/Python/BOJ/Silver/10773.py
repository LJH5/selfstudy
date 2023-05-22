import sys
input = sys.stdin.readline

n = int(input())
stack = [0]

for _ in range(n):
    num = int(input())
    if num:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))