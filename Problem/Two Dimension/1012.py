# bfs
from sys import stdin
from collections import deque

input = stdin.readline

def process():
    global B, M, N, K, visited, cnt

    M, N, K = map(int, input().split())

    B = [[0] * (M) for _ in range(N)]
    visited = [[False] * (M) for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        B[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            elif B[i][j] == 1: 
                bfs(i, j)
                cnt += 1

def bfs(y, x):
    ck = deque([(y, x)])
    visited[y][x] = True
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    
    while ck:
        y, x = ck.popleft()

        for w in range(4):
            ny, nx = y + dy[w], x + dx[w]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if not visited[ny][nx] and B[ny][nx] == 1:
                visited[ny][nx] = True
                ck.append((ny, nx))
                
T = int(input())

for _ in range(T):
    cnt = 0
    process()
    print(cnt)