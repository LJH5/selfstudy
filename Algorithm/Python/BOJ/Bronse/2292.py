# 벌집
'''
등비 수열
1       1
2~7     6
8~19    12
20~37   18
'''

n = int(input())
cut = 1
cnt = 1
while True:
    if n <= cut:
        print(cnt)
        break
    cut += 6*cnt
    cnt += 1
