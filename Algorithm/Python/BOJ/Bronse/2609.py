# 최대공약수와 최소공배수
def find_max_divisor(a, b):
    max_divisor = 1
    divisor = 2
    while divisor <= a and divisor <= b:
        if a % divisor == 0 and b % divisor == 0:
            a //= divisor
            b //= divisor
            max_divisor *= divisor
            continue
        divisor += 1
    return max_divisor


def find_min_multiple(a, b, div):
    min_multiple = a*b
    start = max(a, b)
    if div == 1:                # 최대 공약수가 1이면 
        return min_multiple     # 두 숫자의 곱이 최소 공배수
    while div < a * b:
        if start % a == 0 and start % b == 0:
            min_multiple = start
            break
        start += div
    return min_multiple


num_a, num_b = map(int, input().split())
max_divisor = find_max_divisor(num_a, num_b)
min_multiple = find_min_multiple(num_a, num_b, max_divisor)
print(max_divisor)
print(min_multiple)