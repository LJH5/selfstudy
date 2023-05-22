import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    commend = list(input().split())
    try:
        if commend[0] == 'push':
            q.append(commend[1])
        elif commend[0] == 'pop':
            print(q.popleft())
        elif commend[0] == 'size':
            print(len(q))
        elif commend[0] == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif commend[0] == 'front':
            print(q[0])
        else:
            print(q[-1])
    except:
        print('-1')