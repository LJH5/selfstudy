import sys
input = sys.stdin.readline
M = int(input())
S = [0] * 21
for _ in range(M):
    commend = list(input().split())
    # print(commend)
    if commend[0] == 'add':
        S[int(commend[1])] = 1
    elif commend[0] == 'remove':
        S[int(commend[1])] = 0
    elif commend[0] == 'check':
        if S[int(commend[1])]:
            print(1)
        else:
            print(0)
    elif commend[0] == 'toggle':
        if S[int(commend[1])]:
            S[int(commend[1])] = 0
        else:
            S[int(commend[1])] = 1
    elif commend[0] == 'all':
        S = [0] + [1]*20
    elif commend[0] == 'empty':
        S = [0] * 21