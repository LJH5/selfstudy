# 그냥 조합 2개 뽑기(중복된 조합이 없어야 한다, BC는 CB와 같다, AA나 BB는 취급 안함)
arr = ['A', 'B', 'C']
for i in range(3):
    for j in range(i+1, 3):     # AD는 DA와 같기 때문에 A로 시작되는 모든 조합을 만들면 A는 필요가 없다
        print(arr[i], arr[j])

print('---')

# 중복조합 2개 뽑기(AA나 BB 도 가능)
for i in range(3):
    for j in range(i, 3):
        print(arr[i], arr[j])

print('---')
# 중복 조합, 3개를 이용하여 5개를 만들어라 3H5
# 칸막이를 만든다고 생각하자!
# 0 0 | 0 | 0 0
# 0 | 0 0 0 0 |
# 그렇다면 칸막이를 포함하여 7개의 자리중 칸막이 2개의 위치만 설정하면 된다
sel = [0]*5
def perm(depth):
    if depth == 5:
        print(*sel)
        return

    for i in range(3):
        sel[depth] = arr[i]
        perm(depth + 1)

perm(0)