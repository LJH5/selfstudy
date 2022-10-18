import sys
sys.stdin = open('input.txt', 'r')

def palindrome(arr):
    global result
    for i in range(8):
        for j in range(8-length+1):
            if arr[i][j:j + length][::-1] == arr[i][j:j + length]:
                result += 1

for tc in range(10):
    result = 0
    length = int(input())
    matrix = [input() for i in range(8)]
    sero_matrix = list(zip(*matrix))
    for i in range(len(sero_matrix)):
        sero_matrix[i] = ''.join(sero_matrix[i])

    palindrome(matrix)
    palindrome(sero_matrix)
    print(f'#{tc+1} {result}')