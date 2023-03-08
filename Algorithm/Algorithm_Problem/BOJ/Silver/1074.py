# 배열의 크기는 2 ** n
# 배열을 절반씩 나누어서 순회
# r, c를 몇 번째로 방문했는지 출력
# 재귀를 사용해서 풀어보자

# 2^3 => 2^2 => 2
def cut(n):
    for i in range(0, 2 ** n, 2):
        for j in range(0, 2 ** n, 2):
            print('---------------')
            print('i:', i, 'j:', j)
            for x in range(i, i + 2):
                for y in range(j, j+2):
                    print('x:', x, 'y:', y)
                    if n >= 2:
                        cut(n - 1)


n, r, c = map(int, input().split())
cut(n)
