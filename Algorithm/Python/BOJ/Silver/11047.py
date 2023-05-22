import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = sorted(list(int(input()) for _ in range(n)), reverse=True)

cnt = 0                 # 동전의 개수
for value in values:    # 동전의 가치 내림차순
    cnt += k // value   # k원을 동전의 가치로 나눈 몫을 동전의 개수에 누적
    k %= value          # k원을 동전의 가치로 나눈 나머지로 갱신
print(cnt)              # 동전의 개수 출력