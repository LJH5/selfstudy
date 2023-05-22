cnt = 0
for _ in range(int(input())):
    gift_num = int(input()[2:])
    if gift_num <= 90:
        cnt += 1

print(cnt)
