for tc in range(int(input())):
    A, B = map(int, input().split())
    result = 0
    if A + B > 24:
        result = A + B - 24
    elif A + B == 24:
        result = 0
    else:
        result = A + B
    print(f'#{tc+1} {result}')
