T = int(input())
for tc in range(1, T + 1):
    result = -1
    N = int(input())
    num = round(N**(1/3), 2)
    if num == int(num):
        result = int(num)
    print(f'#{tc} {result}')