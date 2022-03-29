# 개인 풀이
from sys import stdin
input = stdin.readline

# # 변의 길이
# N = int(input())

# # 지점당 가격 리스트 생성
# price = list()
# for _ in range(N):
#     price.append(list(map(int, input().split())))

# # 꽃잎 방향
# dx, dy = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]

# # 꽃 심기
# seed = 3
# result = 0

# for data in price:
#     print(data)
# print()

# while seed:
#     # 변수 초기화(1)
#     min = 1001
#     x, y = 0, 0
    
#     # 탐색 시작
#     for i in range(N):
#         for j in range(N):
#             # 변수 초기화(2)
#             ck = False
#             cost = 0
            
#             # 사전 탐색 종료
#             if 200 < price[i][j]:
#                 continue

#             for c in range(5):
#                 nx, ny = i + dx[c], j + dy[c]
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if price[nx][ny] == 201:
#                         cost = 0
#                         ck = False
#                         break

#                     cost += price[nx][ny]
#                     ck = True
                    
#                 elif 0 > nx or nx >= N or 0 > ny or ny >= N:
#                     cost = 0
#                     ck = False
#                     break

#             # 최소 비용 갱신
#             if ck and 0 <= cost < min:
#                 min, x, y = cost, i, j
#                 print(min, x, y)

#     # 비용 계산
#     seed -= 1
#     result += min

#     # 탐색 완료 표시
#     price[x][y] = 201
#     # print(x, y)

#     for c in range(5):
#         nx, ny = x + dx[c], y + dy[c]
#         # print(nx, ny)
#         price[nx][ny] = 201

#     for data in price:
#         print(data)
#     print()

# print(result)

# 강의 풀이
N = int(input())
G = [list(map(int, input().split())) for i in range(N)]

ans = 10000

dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]

def ck(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower // N
        y = flower % N
        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return 10000

        for w in range(5):
            flow.append((x+dx[w], y+dy[w]))
            ret += G[x+dx[w]][y+dy[w]]

    if len(set(flow)) != 15:
        return 10000
    return ret

for i in range(N*N):
    for j in range(i+1, N*N):
        for k in range(j+1, N*N):
            ans = min(ans, ck([i, j, k]))

print(ans)