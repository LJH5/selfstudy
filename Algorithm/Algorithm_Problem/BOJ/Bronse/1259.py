# 팰린드롬수
while True:
    n = input()
    if n == '0':
        break
    palindrome = n[::-1]
    if palindrome == n:
        print('yes')
    else:
        print('no')