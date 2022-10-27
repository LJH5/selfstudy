def spiral(r, c, cnt):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    visited.add((r, c))
    while cnt < K:
        for k in range(4):
            for _ in range(max(R, C)):
                r += dr[k]
                c += dc[k]
                if r < 1 or r > C or c < 1 or c > R or (r, c) in visited:
                    r -= dr[k]
                    c -= dc[k]
                    break
                visited.add((r, c))
                cnt += 1
                if check(cnt):
                    return r, c


def check(count):
    if count == K:
        return True
    else:
        return False


C, R = map(int, input().split())
K = int(input())

visited = set()
start_r, start_c = 1, 1
start_cnt = 1
if K > C*R:
    print(0)
else:
    if check(start_cnt):
        result = (start_r, start_c)
    else:
        result = spiral(start_r, start_c, start_cnt)

    print(*result)