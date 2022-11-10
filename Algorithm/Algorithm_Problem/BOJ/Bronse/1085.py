# 직사각형에서 탈출

# 현재위치 (x, y)
# 직사각형의 최하단 꼭짓점 (0, 0) 우상단 꼭짓점은 (w, h)
# 현위치에서 직사각형의 경계선까지 가는 최소 거리

x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))