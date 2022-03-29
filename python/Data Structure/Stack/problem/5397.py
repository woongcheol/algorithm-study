# 1차 시도
# from collections import deque
# from sys import stdin

# def keyloger(log):
#     input = deque(log)
#     pt = 0
#     password = deque()
#     back_password = deque()

#     while input:

#         # 화살표 입력
#         if input[0] == '<':
#             if pt >= 1 and input[0] == '<':
#                 pt -= 1
#                 input.popleft()
#             else:
#                 input.popleft()

#         # 화살표 입력
#         elif input[0] == '>':
#             if len(password) > pt and input[0] == '>':
#                 pt += 1
#                 input.popleft()
#             else: 
#                 input.popleft()

#         # 백스페이스
#         elif input[0] == '-':
#             if password and input[0] == '-':
#                 del password[pt-1]
#                 pt -= 1
#                 input.popleft()
#             else: 
#                 input.popleft()

#        # 문자 입력
#         else:
#             if pt == len(password):
#                 password.append(input.popleft())
#                 pt += 1
#             elif pt != len(password):
#                 # 임시 저장
#                 for _ in range(len(password), pt, -1):
#                     back_password.append(password.pop())
                
#                 # 수정
#                 password.append(input.popleft())
#                 pt += 1

#             # 임시 저장된 패스워드 재입력
#             for _ in range(len(back_password)):
#                 password.append(back_password.pop())

#     return list(password)
                
# T = int(input())
# for _ in range(T):
#     log = stdin.readline().strip()
#     print(''.join(keyloger(log)))

# 2차 시도
from sys import stdin

def keyloger(log):
    right_stack = []
    left_stack = []

    for i in log:
        if i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())

        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())

        elif i == '-':
            if left_stack:
                left_stack.pop()

        else:
            left_stack.append(i)
    
    left_stack.extend(reversed(right_stack))
    
    print(''.join(left_stack))
        
T = int(input())
for _ in range(T):
    log = list(stdin.readline().strip())
    keyloger(log)