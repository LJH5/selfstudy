# 16진수를 2진수로 바꾸고(16진수 한 자리 2진수 4자리로 표현)
# 2진수를 7개씩 묶어서
# 10진수로 변환하여 출력
T = int(input())
for tc in range(1, T+1):
    result = []
    hex_dict = {'A': '1010', 'B': '1011', 'C': '1100',
                'D': '1101', 'E': '1110', 'F': '1111'}
    bin = ''
    data = input()
    for i in data:
        if i in hex_dict:                           # A~F 처리
            bin += hex_dict[i]
        else:                                       # 0~9 처리
            for j in range(4):                      # 2진수로 만들기
                check = int(i) // 2**(3-j)          # 2진수의 각 자릿수 구하기
                bin += str(check)                   # 2진 코드에 붙이기
                i = str(int(i) - 2**(3-j)*check)    # 바꾼뒤 나머지 갱신
    for i in range(0, len(bin), 7):
        code = bin[i:i+7]                            # 7개씩 자르기
        tmp = 0
        for j in range(len(code)-1, -1, -1):         # 뒤에서부터 계산
            tmp = int(code[j])*2**(j)