# 1차 시도
# import heapq

# def topology(M):
#     # 변수 선언 및 자료구조 할당
#     heap = list()
#     result = list()
#     indegree = dict()
#     graph = dict()

#     # 그래프 생성 및 진입 차수 초기화
#     for _ in range(M):
#         a, b = map(int, input().split())

#         if not a in graph:
#             graph[a] = [a]
#             indegree[a] = 0
        
#         if not b in graph:
#             graph[b] = [b]
#             indegree[b] = 0

#         graph[a].append(b)
#         indegree[b] += 1

#     # 최초 큐 삽입
#     for data in indegree:
#         if indegree[data] == 0:
#             heapq.heappush(heap, data)
            
#     # 큐가 빌때까지 실행
#     while heap:
#         now = heapq.heappop(heap)
#         result.append(now)

#         for data in graph[now]:
#             indegree[data] -= 1
#             if indegree[data] == 0:
#                 heapq.heappush(heap, data)
    
#     # 결과값 출력
#     for data in result:
#         print(data, end=' ')

# N, M = map(int, input().split())
# topology(M)

# 2차 시도
import heapq

def topology(N, M):
    # 변수 선언 및 자료구조 할당
    heap = list()
    result = list()
    indegree = dict()
    graph = dict()

    # graph, indegree 초기화
    for i in range(1, N+1):
        graph[i] = [i]
        indegree[i] = 0

    # 그래프 생성 및 진입 차수 초기화
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    # 최초 큐 삽입
    for data in indegree:
        if indegree[data] == 0:
            heapq.heappush(heap, data)
            
    # 큐가 빌때까지 실행
    while heap:
        now = heapq.heappop(heap)
        result.append(now)

        for data in graph[now]:
            indegree[data] -= 1
            if indegree[data] == 0:
                heapq.heappush(heap, data)
    
    # 결과값 출력
    for data in result:
        print(data, end=' ')

N, M = map(int, input().split())
topology(N, M)