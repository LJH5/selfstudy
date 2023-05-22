# 수 정렬하기 3
import sys
input = sys.stdin.readline

N = int(input())
numbers = [0]*10001 # 인덱스가 0~10000인 리스트를 만들어 줌
for _ in range(N):
    number = int(input())
    numbers[number] += 1

for i in range(1, 10001):
    for _ in range(numbers[i]):
        print(i)