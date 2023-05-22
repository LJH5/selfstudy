# Hashing
n = int(input())
text = list((ord(i) - 96) for i in input())
code = 0
for i in range(n):
    code += text[i] * 31**i
print(code % 1234567891)
# ord('a') - 96