import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')


def paper_cut(x, y, size):
    cnt = size
    for r in range(x, size - x):
        for c in range(y, size - y):,
            if paper[y][x] != paper[c][r]:
                size //= 3
                for i in range(3):
                    for j in range(3):
                        paper_cut(3*i, 3*j, size)
            else:
                cnt += 1
                if cnt == size:
                    print('yes')

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

paper_cut(0, 0, n)