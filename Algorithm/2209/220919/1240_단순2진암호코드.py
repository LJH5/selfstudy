# 문자는 56자 고정

T = int(input())
for tc in range(1, T+1):
    result = 0
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    for i in range(len(data)):
        idx = data[i][::-1].find('1')
        if idx > 0:
            break
    code = data[i][M-56-idx:M-idx]
    a = []
    for j in range(0, len(code), 7):
        decode = code[j:j+7]
        if decode == '0001101':
            a.append(0)
        elif decode == '0011001':
            a.append(1)
        elif decode == '0010011':
            a.append(2)
        elif decode == '0111101':
            a.append(3)
        elif decode == '0100011':
            a.append(4)
        elif decode == '0110001':
            a.append(5)
        elif decode == '0101111':
            a.append(6)
        elif decode == '0111011':
            a.append(7)
        elif decode == '0110111':
            a.append(8)
        else:
            a.append(9)
    odd = 0
    even = 0
    for k in range(len(a)):
        if k % 2:
            odd += a[k]
        else:
            even += a[k]
    if (even*3 + odd) % 10 == 0:
        result = odd + even
    print(f'#{tc} {result}')
