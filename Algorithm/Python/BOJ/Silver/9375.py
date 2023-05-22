from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    clothes = defaultdict(int)
    for i in range(n):
        name, category = input().split()
        clothes[category] += 1
    cnt = 1
    for key in clothes:             # 알몸만 아니면 되서 하나만 입기 가능 ㅎㄷㄷ
        cnt *= clothes[key] + 1     # 의상 종류별 (개수 + 안입는 경우)를 곱함

    print(cnt-1)    # 알몸인 경우 -1