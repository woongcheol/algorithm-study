from sys import stdin
from collections import deque
import copy
input = stdin.readline

# 구현
def game(start_board, dir, ans):
    board = copy.deepcopy(start_board)

    for i in range(N):
        for j in range(N):
            # 상으로 이동
            if dir == 'top':
                if i == N-1:
                    break
                
                print('top')
                for k in range(i+1, N):
                    # 이동 시키기
                    if board[i][j] == 0 and board[k][j]:
                        board[i][j] = board[k][j]
                        board[k][j] = 0
                    
                    # 이동 및 더하기
                    if board[i][j] == board[k][j]:
                        board[i][j] += board[k][j]
                        board[k][j] = 0
                                    
                    ans = max(ans, board[i][j])
                    break
                print(board)
                print()

            # 하로 이동
            if dir == 'down':
                if i == N-1:
                    break
                print('down')
                for k in range(N-2-i, -1, -1):

                    # 이동 시키기
                    if board[N-1-i][j] == 0 and board[k][j]:
                        board[N-1-i][j] = board[k][j]
                        board[k][j] = 0
                    
                    # 이동 및 더하기
                    if board[N-1-i][j] == board[k][j]:
                        board[N-1-i][j] += board[k][j]
                        board[k][j] = 0
                                    
                    ans = max(ans, board[N-1-i][j])
                    break
                print(board)
                print()

            # 우로 이동
            if dir == 'right':
                if j == N-1:
                    break
                print('right')
                for k in range(N-2-j, -1, -1):

                    # 이동 시키기
                    if board[i][N-1-j] == 0 and board[i][k]:
                        board[i][N-1-j] = board[i][k]
                        board[i][k] = 0
                    
                    # 이동 및 더하기
                    if board[i][N-1-j] == board[i][k]:
                        board[i][N-1-j] += board[i][k]
                        board[i][k] = 0
                                    
                    ans = max(ans, board[i][N-1-j])
                    break
                print(board)
                print()
            
            # 좌로 이동
            if dir == 'left':
                if j == N-1:
                    break
                print('left')
                for k in range(j+1, N):

                    # 이동 시키기
                    if board[i][j] == 0 and board[i][k]:
                        board[i][j] = board[i][k]
                        board[i][k] = 0
                    
                    # 이동 및 더하기
                    if board[i][j] == board[i][k]:
                        board[i][j] += board[i][k]
                        board[i][k] = 0
                                    
                    ans = max(ans, board[i][j])
                    break
                print(board)
                print()

    now_board = copy.deepcopy(board)
    return now_board, ans

def max_sum(board):
    # 초기 환경 설정
    cnt = 5
    result = 0
    ans = 0
    start_board = copy.deepcopy(board)
    game_lst = deque([(start_board, cnt, ans)])

    # BFS
    while game_lst:

        # 최댓값 계산
        board, cnt, ans = game_lst.popleft()
        start_board = copy.deepcopy(board)

        # 블록 이동
        if cnt != 0:
            direction = ['top', 'down', 'right', 'left']
            cnt -= 1
            for dir in direction:
                now_board, ans = game(start_board, dir, ans)
                game_lst.append((now_board, cnt, ans))

        result = max(result, ans)
    
    print(ans)

# 보드 크기
N = int(input())

# 게임판 초기 상태
board = [list(map(int, input().split())) for _ in range(N)]
ck = [[False] * N for _ in range(N)]

if len(board) == 1:
    print(board[0][0])

else:
    max_sum(board)