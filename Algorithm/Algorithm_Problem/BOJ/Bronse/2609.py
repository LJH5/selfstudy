# 최대공약수와 최소공배수
def find_max_divisor(a, b):
    global divisor
    max_divisor = 0
    i = 1
    while i < max(a, b):
        print('====')
        if a % i == 0 and b % i == 0 and max_divisor < i:
            divisor *= i
            max_divisor = i
        i += 1
    return max_divisor


def find_min_multiple(a, b):
    min_multiple = 9999999
    global divisor
    i = 0
    print('------------')
    while i < min_multiple:
        i += divisor
        print('di', divisor)
        print('i', i)
        if find_max_divisor(a, b) == 1:
            min_multiple = a * b
            break
        elif i % a == 0 and i % b == 0 and min_multiple > i:
            min_multiple = i
    return min_multiple


num_a, num_b = map(int, input().split())
divisor = 1
print(find_max_divisor(num_a, num_b))
print(find_min_multiple(num_a, num_b))