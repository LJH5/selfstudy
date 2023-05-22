# 포켓몬 마스터
# N: 포켓몬 도감에 등록된 포켓몬의 수
# M: 내가 맟춰야하는 문제 수
# 2 <= 이름 길이 <= 20
# 도감번호는 1부터 시작이다!!
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

N, M = map(int, input().split())
poketmons = dict()

for i in range(1, N + 1):
    poketmon = input()
    poketmons[i] = poketmon
    poketmons[poketmon] = i

for j in range(M):
    quest = input()
    if quest in poketmons.keys():
        print(poketmons[quest])
    else:
        print(poketmons[int(quest)])