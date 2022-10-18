import sys
sys.stdin = open('input.txt', 'r')

def palindrome(arr):
    global result
    for i in range(100):
        flag = False
        for j in range(100, -1, -1):
            if result > j:           # 백트래킹
                break
            for k in range(100 - j + 1):
                if arr[i][k:k+j][::-1] == arr[i][k:k+j]:
                    if result < j:
                        result = j
                    flag = True     # 백트래킹
                    break
            if flag:                # 백트래킹
                break


for _ in range(10):
    result = 0
    tc = int(input())
    matrix = [input() for i in range(100)]
    sero_matrix = list(zip(*matrix))
    for i in range(len(sero_matrix)):
        sero_matrix[i] = ''.join(sero_matrix[i])

    palindrome(matrix)
    palindrome(sero_matrix)
    print(f'#{tc} {result}')