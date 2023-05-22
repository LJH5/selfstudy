import sys
input = sys.stdin.readline

n = int(input())
nums = list(int(input()) for _ in range(n))

stack = []
result = []                             # +, - 연산을 저장할 리스트
idx = 0                                 # 입력된 수열의 인덱스
for i in range(1, n + 1):               # 1 ~ n 까지 반복
    stack.append(i)                     # 일단 push 연산
    result.append('+')                  # 연산을 저장
    for _ in range(len(stack)):         # 빼낸 뒤 stack의 마지막 숫자가 다음 수열의 값이면 또 빼야하기 때문에 반복문을 사용
        if stack[-1] == nums[idx]:      # 가장 마지막의 숫자가 수열의 숫자면
            stack.pop()                 # pop연산
            result.append('-')          # 연산을 저장
            idx += 1                    # 다음 수열의 숫자로

if stack:                               # 스택에 숫자가 남았으면 불가능
    print('NO')
else:                                   # 스택이 비었으면 가능
    for i in result:                    # 저장한 연산을
        print(i)                        # 한줄씩 출력
