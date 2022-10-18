T = int(input())
for tc in range(1, T+1):
    result = []
    hex_dict = {'A': 10, 'B': 11, 'C': 12,
                'D': 13, 'E': 14, 'F': 15}
    bin = ''
    N, data = input().split()
    for i in data:
        if i in hex_dict:                       # A~F 처리
            i = hex_dict[i]                     # 해당하는 10진수로 바꿔줌
        for j in range(4):                      # 2진수로 만들기
            check = int(i) // 2**(3-j)          # 2진수의 각 자릿수 구하기
            bin += str(check)                   # 2진 코드에 붙이기
            i = str(int(i) - 2**(3-j)*check)    # 바꾼뒤 나머지 갱신
    print(f'#{tc} {bin}')