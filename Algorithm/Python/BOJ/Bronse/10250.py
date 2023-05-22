# ACM 호텔
# 층수는 사람수 % 높이 (단, 0이 될 경우는 높이와 층이 같다)
# 번호는 사람수 // 높이 + 1
import sys
input = sys.stdin.readline
for tc in range(int(input())):
    h, w, customer = map(int, input().split())
    y = customer % h
    x = customer // h + 1
    if y == 0:
        y = h
        x = customer // h
    print(str(y) + str(x).zfill(2))
