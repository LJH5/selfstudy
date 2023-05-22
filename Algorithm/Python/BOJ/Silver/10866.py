from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

q = deque()
for _ in range(n):
    commend = list(input().split())
    try:
        if commend[0] == 'push_front':
            q.appendleft(commend[1])
        elif commend[0] == 'push_back':
            q.append(commend[1])
        elif commend[0] == 'pop_front':
            print(q.popleft())
        elif commend[0] == 'pop_back':
            print(q.pop())
        elif commend[0] == 'size':
            print(len(q))
        elif commend[0] == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif commend[0] == 'front':
            print(q[0])
        elif commend[0] == 'back':
            print(q[-1])
    except:
        print('-1')
