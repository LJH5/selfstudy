import heapq

arr = [9, 2, 4, 5, 1, 6, 7]

heapq.heapify(arr)
print(arr)
heapq.heappush(arr, 3)
print(arr)
pooop = heapq.heappop(arr)
print(arr, pooop)
r = heapq.heappushpop(arr, 10)
print(arr, r)
heapq.heapreplace(arr, 5)
print(arr)