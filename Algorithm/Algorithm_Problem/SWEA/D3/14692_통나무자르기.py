# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    if n%2:
        print(f'#{test_case} Bob')
    else:
        print(f'#{test_case} Alice')