# 난쟁이 9명 중 7명 고정
short_mans = [int(input()) for _ in range(9)]
result = []
for i in range(1 << 9):
    selected = []

    for j in range(9):
        if i & (1 << j):
            selected.append(short_mans[j])

    if sum(selected) == 100 and len(selected) == 7:   # 부분집합 7개 짜리의 합이 100
        result = sorted(selected)
        break

for i in result:
    print(i)