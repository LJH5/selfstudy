import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)

stack = [1]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in adj_list[current]:
        if destination not in visited:
            stack.append(destination)

print(len(visited) - 1)

