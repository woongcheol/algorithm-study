import heapq

N = int(input())
heap = list()
sum = 0
result = 0
for _ in range(N):
    data = int(input())
    heapq.heappush(heap, data)

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum = a + b
    result += sum
    heapq.heappush(heap, sum)

print(result)

