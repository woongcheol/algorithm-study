from collections import deque

# BFS
def bfs(n):
    global cnt
    q = deque([n])

    while q:
        now = q.popleft()
        visited[now] = 1
        for e in vertex_list[now]:
            if not visited[e]:
                cnt += 1
                visited[e] = 1
                q.append(e)
    print(cnt)

# DFS
def dfs(n):
    global cnt
    stack = list()
    stack.append(n)

    while stack:
        now = stack.pop()
        visited[now] = 1
        for e in vertex_list[now]:
            if not visited[e]:
                cnt += 1
                visited[e] = 1
                stack.append(e)

    print(cnt)

# 정점 입력
v = int(input())

# 간선 입력
e = int(input())

# 정점 리스트 생성
vertex_list = [[] for _ in range(v+1)]

# 방문 리스트 생성
visited = [0] * (v + 1)

# 기타 변수
cnt = 0

for _ in range(e):
    x, y = map(int, input().split())
    vertex_list[x].append(y)
    vertex_list[y].append(x)

# bfs(1)
dfs(1)