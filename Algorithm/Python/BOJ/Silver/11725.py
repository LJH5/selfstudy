import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def find_parent(V, tree):
    q = deque([1])
    parent = [0] * (V + 1)
    while q:
        # print(q)
        # print(parent)
        now = q.popleft()
        for node in tree[now]:
            # print(node)
            if parent[node] == 0 and node != 1:
                parent[node] = now
                q.append(node)
    for i in range(2, V + 1):
        print(parent[i])


V = int(input())
E = V - 1

tree = defaultdict(list)

for _ in range(E):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

# print(tree)

find_parent(V, tree)