from collections import deque

n, k = map(int, input().split())
q = deque()
for i in range(1, n+1):
    q.append(i)
result = []
while q:
    for _ in range(k-1):
        num = q.popleft()
        q.append(num)
    num = q.popleft()
    result.append(num)

ans = "<"
for i in range(len(result)):
    ans += str(result[i])
    if i < len(result)-1:
        ans += ", "
    else:
        ans += ">"
print(ans)