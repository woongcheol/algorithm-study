import heapq
def organize_book(location, M):
    
    # 책 정렬
    left = list()
    right = list()
    
    # 가장 멀리있는 위치
    largest = max(max(location), -min(location))

    for num in location:
        if num > 0:
            heapq.heappush(right, -num)
        else:
            heapq.heappush(left, num)

    # 1회 최대 운반량 계산
    result = 0
    while left:
        result += heapq.heappop(left)*2
        for _ in range(M-1):
            if left:
                heapq.heappop(left)
            else:
                break

    while right:
        result += heapq.heappop(right)*2
        for _ in range(M-1):
            if right:
                heapq.heappop(right)
            else:
                break

    # 합계
    print(-result - largest)

N, M = map(int, input().split())
location = list(map(int, input().split()))

organize_book(location, M)