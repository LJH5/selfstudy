import sys
sys.stdin = open('input.txt', 'r')
# 100x100 평면
# 글자는 A, B, C 중 하나이다
# 가장 긴 회문을 구하시오

# 리스트의 요소인 문자열의 회문을 찾는 함수
def find_palindrome(table_list):
    max_len = 0
    for txt in table_list:
        # 반띵해서 두개 비교하여 회문 검사
        # i는 100~2까지 반띵하기 때문에 2개 이상일때까지 회문 검사
        for i in range(100, 1, -1):
            # i(회문의 길이)에 따라 구간이 달라짐 예) i=99, 0~49/98~50과 1~50/99~51두가지 경우 나옴
            for j in range(100-i+1):
                start = txt[j:i//2+j]
                end = txt[(i-1)+j:(i-i//2-1)+j:-1]
                if start == end and i > max_len:
                    max_len = i
    return max_len

#총 10번의 테스트 케이스
for _ in range(10):
    result = 0  # 가로, 세로 회문 중 가장 긴 값을 저장할 변수
    tc = int(input())
    table_list = [input() for _ in range(100)]

    # 가로 회문 길이
    garo_len = find_palindrome(table_list)
    # 세로 리스트만들기
    sero_list = list(zip(*table_list))
    for i in range(len(sero_list)):
        sero_list[i] = ''.join(sero_list[i])
    # 세로 회문 길이
    sero_len = find_palindrome(sero_list)

    if garo_len >= sero_len:
        result = garo_len
    else:
        result = sero_len

    print(f'#{tc} {result}')
        