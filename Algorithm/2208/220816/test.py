a = ['abc', 'def', 'ghi']
# 각 요소 zip(튜플로 나옴) -> list로 저장
c = list(zip(*a))
# 튜플로 저장되어 있는 각 요소 문자열로
for i in range(len(c)):
    c[i] = ''.join(c[i])
print(c)
