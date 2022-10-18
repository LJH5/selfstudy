T = int(input())
for tc in range(1, T+1):
    result = []
    hex_dict = {'A': '1010', 'B': '1011', 'C': '1100',
                'D': '1101', 'E': '1110', 'F': '1111'}
    pat_dict = {'001101': 0, '010011': 1, '111011': 2,
                '110001': 3, '100011': 4, '110111': 5,
                '001011': 6, '111101': 7, '011001': 8,
                '101111': 9}
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

    bin = list(bin)

    for i in range(len(bin)-5):                      # 패턴은 6자리
        for key in pat_dict.keys():                  # 패턴을 하나씩 가져옴
            if ''.join(bin[i:i+6]) == key:           # 패턴이 일치하면
                for j in range(6):
                    bin[i+j] = '-'                   # 사용한 패턴을 '-' 로 바꾸고
                result.append(pat_dict[key])         # 결과값에 암호를 저장

    print(*result)