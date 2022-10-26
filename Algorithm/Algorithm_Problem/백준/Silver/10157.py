def spiral():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c = 1, 1
    for k in range(4):
        for _ in range(max(R, C)):
            if not(1 <= r < R and 1 <= c < C):
                r -= dr[k]
                c -= dc[k]
                break
            print(r, c)
            r += dr[k]
            c += dc[k]


C, R = map(int, input().split())
K = int(input())

spiral()
