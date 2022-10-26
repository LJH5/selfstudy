def cycle():
    rotate(1, 1, 1)


def rotate(r, c, cnt):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    visited = set()
    visited.add((r, c))
    for k in range(4):
        print('=========')
        for _ in range(max(R, C)):
            r += dr[k]
            c += dc[k]
            if r < 1 or r >= R or c < 1 or c >= C or (r, c) in visited:
                r -= dr[k]
                c -= dc[k]
                break
            visited.add((r, c))
            cnt += 1
            print(r, c)
            if cnt == num:
                return r, c


C, R = map(int, input().split())
num = int(input())
if num > R*C:
    print(0)
elif num == 1:
    print(1, 1)
else:
    cycle()