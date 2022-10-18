def recursive_power(x, n):
    if n == 1:
        return x

    # 짝수승인 경우
    if not n % 2:
        y = recursive_power(x, n/2)
        return y*y

    # 홀수승인 경우
    else:
        y = recursive_power(x, (n-1)/2)
        return y*y*x

print(recursive_power(2, 100))