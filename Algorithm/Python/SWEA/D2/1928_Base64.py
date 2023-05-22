decode_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/'
          ]

for tc in range(int(input())):
    result = ''      
    code_list = []
    for i in list(input()):                         # 문자를 입력 받고
        decode = decode_list.index(i)               # 해당하는 문자의 값를 decode에 저장
        bin_decode = format(decode, 'b')            # 값을 2진수로 표현
        code_list.append(str(bin_decode).zfill(6))  # 6자리 2진수 문자열로 만들어서 배열에 저장
    code_str = ''.join(code_list)                   # 2진수 문자열로 만든 코드를 한줄로 이어붙임
    for i in range(0, len(code_str), 8):
        dec_decode = int('0b'+code_str[i:i+8], 2)   # 8개씩 끊어서 10진수로 표현
        result += chr(dec_decode)                   # 10진수로 표현한 숫자를 아스키로 변환
    print(f'#{tc+1} {result}')
