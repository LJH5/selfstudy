arr = [1, 2, 3, 4, 5]
# 비트 연산자를 이용한 부분집합
print('비트 연산자')
for i in range(1 << len(arr)):
    tmp = []
    for j in range(len(arr)):
        if i & (1 << j):
            tmp.append(arr[j])
    print(tmp)

# 재귀 함수를 이용한 부분집합
check = [0] * 5

def powerset(idx):
    if idx == 5:
        result = []
        for j in range(5):
            if check[j] == 1:
                result.append(arr[j])
        print(result)
        return

    check[idx] = 0
    powerset(idx+1)

    check[idx] = 1
    powerset(idx+1)
    
print('재귀 함수')
powerset(0)
