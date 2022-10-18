import sys
sys.stdin = open('input.txt', 'r')
# [1, B, 3,| B, 3 , B,| 8, 1, F,| 7, 5, E]
# 다이얼은 시계방향으로 돌리면 숫자가 시계방향으로 돌아간다
# 마지막 인덱스가 0번으로 온다
# 자물쇠의 비밀번호는 보물상자의 숫자로 만들수 있는 모든 수 중 k번째로 큰 수
# 부분집합을 만들어서 처리하나? 시간 초과 뜨지 않을 까?
# 16진수는 0x로 표현한다

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    code_len = N//4                             # 코드의 길이
    code = input()
    ex_code = code * 2                          # 아몰라 코드 냅다 2배로 늘린 것
    code_set = set()                            # 중복을 제거한 코드를 저장할 set
    decode_list = []                            # 10진수로 표현된 코드를 저장할 list
    for i in range(len(ex_code)):               # 슬라이싱은 어차피 인덱스 오류 안나니까 무지성 길이 넣기
        code_set.add(ex_code[i:i+code_len])     # 코드 길이만큼 잘라서 저장

    for i in code_set:                          # 중복 제거된 16진법 코드
        decode_list.append(int(i, 16))          # 10진수로 바꾸기
    decode_list.sort(reverse=True)              # 내림차순으로 정렬
    result = decode_list[K-1]                   # 인덱스는 0번 부터 시작함 K-1번 index가 K번째 큰 값

    print(f'#{tc} {result}')
