import sys; sys.stdin = open('6485.txt')

'''
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N ( 1 ≤ N ≤ 500 )이 주어진다.
다음 N개의 줄의 i번째 줄에는 두 정수 Ai, Bi ( 1 ≤ Ai ≤ Bi ≤ 5,000 )가 공백 하나로 구분되어 주어진다.
다음 줄에는 하나의 정수 P ( 1 ≤ P ≤ 500 )가 주어진다.
다음 P개의 줄의 j번째 줄에는 하나의 정수 Cj ( 1 ≤ Cj ≤ 5,000 ) 가 주어진다.
'''
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    stop = [0] * (5000 + 1)

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            stop[i] += 1

    P = int(input())
    nums = [int(input()) for _ in range(P)]

    print(f'#{tc}', end=' ')
    result = []
    for i in nums:
        result.append(stop[i])
    print(' '.join(map(str, result)))
