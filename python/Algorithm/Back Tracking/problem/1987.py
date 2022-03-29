import sys
input = sys.stdin.readline

def dfs(x, y):
    global result
    q = set()
    q.add((x, y, array[x][y]))
    
    while q:
        x, y, step = q.pop()
        result = max(result, len(step))
        for dir in direction:
            dx, dy = dir

            # 이동 시 방향설정
            nx = x + dx
            ny = y + dy

            # 방향 조건
            cond_x = nx >= 0 and R > nx
            cond_y = ny >= 0 and C > ny

            # 조건 만족 시 이동
            if cond_x and cond_y:
                if array[nx][ny] not in step:
                    q.add((nx, ny, step + array[nx][ny]))
                
R, C = map(int, input().split())
array = [input().strip() for _ in range(R)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0
dfs(0, 0)
print(result)