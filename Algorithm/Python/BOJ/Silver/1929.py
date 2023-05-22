# 에라토스테네스의 체
# 2가 소수 -> 2의 배수는 소수 아님
# 3이 소수 -> 3의 배수는 소수 아님


m, n = map(int, input().split())

for i in range(m, n + 1):
    if i == 1:                           # 1은 제외
        continue
    for j in range(2, int(i**0.5) + 1):  # n까지 수의 최대 약수는 n^0.5 이하이다
        if i % j == 0:                   # 약수가 존재하므로 소수가 아님
            break
    else:                                # break에 안 걸리면 소수
        print(i)