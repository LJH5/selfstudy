# 숫자 카드 2
import sys


def makeCardDict():                     # 숫자를 key, 개수를 value로 가지는 딕셔너리 만들기
    for num in cards:
        if num in my_card.keys():
            my_card[num] += 1           # 있는 슷지면 개수 +1
        else:
            my_card[num] = 1            # 없는 숫지면 새로 만들고 개수 1로


N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
my_card = dict()

makeCardDict()
for number in numbers:
    if number in my_card.keys():        # 상근이가 가지고 있는 숫자이면
        print(my_card[number], end=' ') # 그 숫자의 값 출력
    else:
        print(0, end=' ')               # 가지고 있지 않은 숫자이면 0