# from sys import stdin
# from collections import deque
# import copy
# input = stdin.readline

# # 구현
# def game(start_board, dir, ans):
#     board = copy.deepcopy(start_board)

#     for i in range(N):
#         for j in range(N):
#             # 상으로 이동
#             if dir == 'top':
#                 print('top')
#                 for k in range(i+1, N):
#                     # 이동
#                     if board[k][j]:
#                         if board[i][j] == 0:
#                             board[i][j] = board[k][j]
#                             board[k][j] = 0

#                         elif board[i][j] == board[k][j]:
#                             board[i][j] += board[k][j]
#                             board[k][j] = 0
#                             break
#                         else:
#                             break

#                         # 더하기
#                         for l in range(k+1, N):
#                             if board[l][j] == 0:
#                                 continue
#                             elif board[l][j] != board[i][j]:
#                                 break
#                             if board[i][j] == board[l][j]:
#                                 board[i][j] += board[l][j]
#                                 board[l][j] = 0
#                                 break
#                         break
                                    
#                     ans = max(ans, board[i][j])
#                 print(board)
#                 print()

#             # 하로 이동
#             if dir == 'down':
#                 print('down')
#                 for k in range(N-2-i, -1, -1):

#                     # 이동
#                     if board[k][j]:
#                         if board[N-1-i][j] == 0:
#                             board[N-1-i][j] = board[k][j]
#                             board[k][j] = 0

#                         elif board[N-1-i][j] == board[k][j]:
#                             board[N-1-i][j] += board[k][j]
#                             board[k][j] = 0
#                             break
#                         else:
#                             break                    

#                         # 더하기
#                         for l in range(k-1, -1, -1):
#                             if board[l][j] == 0:
#                                 continue
#                             elif board[l][j] != board[N-1-i][j]:
#                                 break
#                             if board[N-1-i][j] == board[l][j]:
#                                 board[N-1-i][j] += board[l][j]
#                                 board[l][j] = 0
#                                 break
#                         break
                                    
#                     ans = max(ans, board[N-1-i][j])
#                 print(board)
#                 print()

#             # 우로 이동
#             if dir == 'right':
#                 print('right')
#                 for k in range(N-2-j, -1, -1):
                    
#                     # 이동
#                     if board[i][k]:
#                         if board[i][N-1-j] == 0:
#                             board[i][N-1-j] = board[i][k]
#                             board[i][k] = 0

#                         elif board[i][N-1-j] == board[i][k]:
#                             board[i][N-1-j] += board[i][k]
#                             board[i][k] = 0
#                             break
#                         else:
#                             break
                    
#                     # 이동 및 더하기
#                         for l in range(k-1, -1, -1):
#                             if board[i][l] == 0:
#                                 continue
#                             elif board[i][l] != board[i][N-1-j]:
#                                 break
#                             if board[i][N-1-j] == board[i][l]:
#                                 board[i][N-1-j] += board[i][l]
#                                 board[i][l] = 0
#                                 break
#                         break
                                    
#                     ans = max(ans, board[i][N-1-j])
#                 print(board)
#                 print()
            
#             # 좌로 이동
#             if dir == 'left':
#                 print('left')
#                 for k in range(j+1, N):

#                     # 이동
#                     if board[i][k]:
#                         if board[i][j] == 0:
#                             board[i][j] = board[i][k]
#                             board[i][k] = 0
#                         elif board[i][j] == board[i][k]:
#                             board[i][j] += board[i][k]
#                             board[i][k] = 0
#                             break
#                         else:
#                             break
                    
#                         # 이동 및 더하기
#                         for l in range(k+1, N):
#                             if board[i][l] == 0:
#                                 continue
#                             elif board[i][l] != board[i][j]:
#                                 break
#                             if board[i][j] == board[i][l]:
#                                 board[i][j] += board[i][l]
#                                 board[i][l] = 0
#                                 break
#                         break
                                           
#                     ans = max(ans, board[i][j])
#                 print(board)
#                 print()


#     now_board = copy.deepcopy(board)
#     return now_board, ans

# def max_sum(board):
#     # 초기 환경 설정
#     cnt = 5
#     result = 0
#     ans = 0
#     start_board = copy.deepcopy(board)
#     game_lst = deque([(start_board, cnt, ans)])

#     # BFS
#     while game_lst:
#         # 최댓값 계산
#         board, cnt, ans = game_lst.popleft()
        
#         # 블록 이동
#         if cnt != 0:
#             cnt -= 1
#             start_board = copy.deepcopy(board)
#             direction = ['top', 'down', 'right', 'left']
#             for dir in direction:
#                 now_board, ans = game(start_board, dir, ans)
#                 game_lst.append((now_board, cnt, ans))

#         result = max(result, ans)
    
#     print(result)

# # 보드 크기
# N = int(input())

# # 게임판 초기 상태
# board = [list(map(int, input().split())) for _ in range(N)]

# if len(board) == 1:
#     print(board[0][0])

# else:
#     max_sum(board)

# 강의 풀이
from copy import deepcopy

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]

def rotate90(B, N):
    NB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            NB[j][N-i-1] = B[i][j]
    return NB

def convert(lst, N):
    new_list = [i for i in lst if i]
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i]
    return new_list + [0] * (N-len(new_list))

def dfs(N, B, count):
    ret = max([max(i) for i in B])
    if count == 0:
        return ret
    for _ in range(4):
        X = [convert(i, N) for i in B]
        if X != B:
            ret = max(ret, dfs(N, X, count-1))
        B = rotate90(B, N)

    return ret

print(dfs(N, B, 5))
