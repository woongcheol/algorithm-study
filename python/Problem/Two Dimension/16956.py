from sys import stdin

input = stdin.readline
R, C = map(int, input().split())
M = list()

for _ in range(R):
    line = input().strip()
    M.append(list(line))

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
ck = False

# 맵 탐색
for i in range(R):
    for j in range(C):

        # 늑대 근처 양 확인
        if M[i][j] == 'W':
            for n in range(4):
                nx, ny = i + dx[n], j + dy[n]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                elif M[nx][ny] == 'S':
                    ck = True
                    break
                else:
                    if M[nx][ny] != 'W':
                        M[nx][ny] = 'D'

# 결과 출력
if ck:
    print(0)
else:
    print(1)
    for line in M:
        print(''.join(line))