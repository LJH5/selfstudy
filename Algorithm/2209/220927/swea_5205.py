def lomuto(low, high):

    def partition(low, high):       # 칸막이의 위치, 불완전 정렬
        pivot = a[high]
        left = low

        for right in range(low, high):
            if a[right] < pivot:
                a[left], a[right] = a[right], a[left]
                left += 1

        a[left], a[high] = a[high], a[left]
        return left

    if low < high:
        pivot = partition(low, high)
        lomuto(low, pivot-1)
        lomuto(pivot+1, high)

a = [2, 8, 7, 1, 3, 5, 6, 4]
lomuto(0, len(a)-1)
print(a)