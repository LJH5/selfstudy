import sys
input = sys.stdin.readline
# 해당 방식으로 입력받으면 '\n'이 들어가는 것을 주의하자!!!
n = int(input())
stack = []

for _ in range(n):
    commend = list(input().split())
    try:
        if commend[0] == 'push':
            stack.append(commend[1])
        elif commend[0] == 'pop':
            print(stack.pop())
        elif commend[0] == 'size':
            print(len(stack))
        elif commend[0] == 'empty':
            if stack:
               print(0)
            else:
                print(1)
        else:
            print(stack[-1])
    except:
        print('-1')