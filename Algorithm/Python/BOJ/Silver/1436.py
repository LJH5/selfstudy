n = int(input())
cnt = 0
i = 666
while True:
    if '666' in str(i):
        cnt += 1
        if cnt == n:
            result = i
            break
    i += 1
print(result)