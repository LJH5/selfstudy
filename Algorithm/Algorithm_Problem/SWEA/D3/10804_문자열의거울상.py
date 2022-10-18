# 문자열 좌우 반전 후
# q -> p, p -> q, d -> b, b -> d
T = int(input())
for tc in range(1, T+1):
    result = ''
    txt = input()[::-1]
    for i in txt:
        if i == 'q':
            result += 'p'
        elif i == 'p':
            result += 'q'
        elif i == 'b':
            result += 'd'
        else:
            result += 'b'
    print(f'#{tc} {result}')