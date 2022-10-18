import sys
sys.stdin = open('input.txt', 'r')

def com(idx, sidx):
    global result
    if sidx == 3:
        if result < sum(sel) <= M:
            result = sum(sel)
        return
    if idx == N:
        return

    sel[sidx] = cards[idx]
    com(idx+1, sidx+1)
    com(idx+1, sidx)

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0
sel = [0, 0, 0]

com(0, 0)

print(result)