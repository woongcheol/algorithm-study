from collections import deque

def bfs(n):
    q = deque([n])
    count = 1
    visited = [False] * (N+1)
    visited[n] = True
    while q:
        now = q.popleft()
        for e in adj[now]:
            if not visited[e]:
                count += 1
                visited[e] = True
                q.append(e)

    return count

N, M = map(int, input().split())

adj = [[]for _ in range(N+1)]

for _ in range(M):
        a, b = map(int, input().split())
        adj[b].append(a)

result = list()
max = -1

for i in range(1, N+1):
    c = bfs(i)
    if c > max:
        result = [i]
        max = c
    elif c == max:
        result.append(i)
        max = c

for e in result:
    print(e, end=" ")