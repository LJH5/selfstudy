# 암호는 총 8개의 슛자로 이루어져 있다
# 앞 7자리는 상픔의 고유번호, 뒤 1자라는 검증코드
# 홀수자리 합 * 3 + 짝수번호 합 + 검증코드는 10의 배수(인덱스가 짝수 -> 홀수자리)
# 배열은 16진수 -> 2진수로 변환해 확인
# 맨뒷자리는 무조건 1이니까 맨뒤가 1인 것 부터 56자리를 가져옴
# 코드가 두꺼워져도 비율은 일정하다
# 암호코드가 56자리 -> 2진수를 7자리씩 끊어서 읽음
# 일단 56개부터 하고 유효한 코드가 나오지 않으면 56*n으로 점점늘려가면서 처리

# 일단 

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    result = 0
    N, M = map(int, input().split())
    code_set = set()
    hex_dict = {'A': '1010', 'B': '1011', 'C': '1100',
                'D': '1101', 'E': '1110', 'F': '1111'}
    decode_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
                   '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    for i in range(N):
        data = input()
        if data == '0'*M or data in code_set:          # 의미있는 코드가 아니면
            continue                                   # 다음으로
        code_set.add(data)                             # 의미있는 코드는 code_set에 추가

    for code in code_set:                              # 코드 하나를 가지고 옴
        bin_str = ''
        for i in code:
            if i in hex_dict:                          # A~F 처리
                bin_str += hex_dict[i]
            else:                                      # 0~9 처리
                for j in range(4):                     # 2진수로 만들기
                    check = int(i) // 2 ** (3 - j)     # 2진수의 각 자릿수 구하기
                    bin_str += str(check)              # 2진 코드에 붙이기
                    i = str(int(i)-2**(3-j)*check)     # 바꾼뒤 나머지 갱신

        idx = bin_str[::-1].find('1')                  # 뒤에서부터 1을 찾음(코드의 마지막은 1)
        decode_str = bin_str[len(bin_str) - idx - 56:len(bin_str) - idx]
        decode_list = []
        for j in range(0, len(decode_str), 7):
            decode = decode_str[j:j + 7]               # 56자리의 코드를
            decode_list.append(decode_dict[decode])    # 8자리 코드로 리스트에 저장

        odd = 0
        even = 0
        for k in range(len(decode_list)-1):            # 마지막 자리인 검증 코드를 빼고
            if k % 2:                                  # 짝수 자리(인덱스는 홀수)
                odd += decode_list[k]                  # 짝수 자리끼리 더하기
            else:                                      # 홀수 자리(인덱스는 짝수)
                even += decode_list[k]                 # 홀수 자리끼리 더하기
        if (even*3 + odd + decode_list[7]) % 10 == 0:  # (홀수 자리)*3 + 짝수자리 + 검증 코드가 10의 배수이면 유효한 코드
            result = odd + even + decode_list[7]
    print(f'#{tc} {result}')
