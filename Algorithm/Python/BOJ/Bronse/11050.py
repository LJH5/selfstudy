# 이항 계수 1
# n!/(k!(n-k)!)
def factorial(num):
    fac = 1
    for i in range(2, num+1):
        fac *= i
    return fac


n, k = map(int, input().split())
n_fac = factorial(n)
k_fac = factorial(k)
n_k_fac = factorial(n-k)
print(int(n_fac/(k_fac*n_k_fac)))
