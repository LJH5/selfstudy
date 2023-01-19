n = int(input())
stack = []

for _ in range(n):
    commend = input()
    if 'push' in commend:
        stack.append(commend[-1])
    elif 'pop' in commend:
        stack.append()