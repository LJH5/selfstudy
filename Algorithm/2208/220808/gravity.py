T = int(input())
for tc in range(T):
    n = int(input())
    box_height = list(map(int, input().split()))
    # 각 상자열의 꼭대기에 있는 상자의 낙차구하기
    # 낙차는 자신의 높이 보다 낮은 박스의 갯수
    result = 0
    for i in range(0, n+1):
        nakcha = 0
        # 자신 다음 것 부터 비교
        for j in range(i+1, n):
            if box_height[i] > box_height[j]:
                nakcha += 1
        if result < nakcha:
            result = nakcha
    print(f'#{tc} {result}')