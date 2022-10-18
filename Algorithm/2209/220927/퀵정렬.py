def quick_sort(l, r):
    if l < r:
        s = partition(l, r)
        quick_sort(l, s-1)
        quick_sort(s+1, r)

def partition(l, r):
    p = A[l]
    i = l                               # i는 왼쪽에서 시작
    j = r                               # j는 오른쪽에서 시작
    while i <= j:                       # 겹칠때까지 반복해야함
        while i <= j and A[i] <= p:     # 피봇보다 큰 값을 찾는다
            i += 1
        while i <= j and A[j] >= p:     # 피봇보다 작은 값을 찾는다
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input().split()))
    N = len(A)
    quick_sort(0, N - 1)
    print(*A)








