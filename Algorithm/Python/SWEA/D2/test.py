def danjo(num, res, lengh):
    if num == 0:
        return True
    print('num', num)
    print('res', res)
    if num%10 <= res:
        danjo(num//10, num%10, lengh-1)
    else:
        return False


print(danjo(1234//10, 1234%10, len(str(1234))))