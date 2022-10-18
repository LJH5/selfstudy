# a와 b사이의 숫자중 제곱팰린드롬의 개수를 구하여라 1<= a <= b <= 1000
# 재곱팰린드롬은 숫자와 그 숫자의 제곱근의 좌우가 같은 것을 말한다
T = int(input())
for tc in range(1, T+1):
    result = 0
    start, end = map(int, input().split())
    check = {484, 121, 9, 4, 1}               # 1~1000사이의 재곱팰린드롬
    for num in range(start, end+1):
        if num in check:
            result += 1
    print(f'#{tc} {result}')


