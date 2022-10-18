import heapQ  # 힙큐 모듈은 '최소힙'이다!

# 일반적인 잡 리스트를 힙으로 만들어버리기 => 원본을 바꿔버린다는 게 포인트
arr = [2, 4, 7, 3, 5, 8]
heapQ.heapify(arr)
print('#1 힙으로 만들기', arr)  # [2, 3, 7, 4, 5, 8]
print('------------------------------------')

# 힙 푸시
print('#2 힙푸시')
heap = []
heapQ.heappush(heap, 8)  # 리턴값이 없어서 None임
print(heap)
heapQ.heappush(heap, 5)
print(heap)
heapQ.heappush(heap, 3)
print(heap)
heapQ.heappush(heap, 6)
print(heap)
print('------------------------------------')

# 힙합
print('#3 힙합')
heapQ.heappop(heap)
print(heap)
heapQ.heappop(heap)
print(heap)
heapQ.heappop(heap)
print(heap)
res = heapQ.heappop(heap)
print(heap)
# 없는 상태에서 뽑으려면 index out of range가 난다!
# heapq.heappop(heap)
print('res에 담김: ', res)
print('------------------------------------')

# 힙에는 그럼 숫자만 넘길수있나?
print('#4 튜플 넘기기')
min_heap = []
heapQ.heappush(min_heap, (3, 5))  # '앞쪽' 숫자를 기준으로 최소힙을 만든다!
heapQ.heappush(min_heap, (1, 6))
heapQ.heappush(min_heap, (4, 'hihi'))  # 그러니까 앞에만 숫자이면 됨
# heapq.heappush(min_heap, ('그러니까 이건 오류남', 'hihi'))
print(min_heap)
print('------------------------------------')

# 그러면 최대힙은 어떻게 할건데? => 앞쪽을 기준으로 최소힙을 만든다는 점을 활용
# (내가 구하고자 하는 값의 -를 줘서 우선순위가 거꾸로 하게 함, 진짜 내가 활용하고 싶은 숫자)
print('#5 최대힙')
max_heap = []
heapQ.heappush(max_heap, (-3, 3))
heapQ.heappush(max_heap, (-5, 5))
heapQ.heappush(max_heap, (-4, 4))
print(max_heap)