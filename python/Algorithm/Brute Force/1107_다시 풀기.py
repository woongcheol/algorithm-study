# # 1차 시도 - 특정 케이스 오답
# from cmath import inf
# from sys import stdin
# input = stdin.readline

# def min_num(temp, num):
#     up = num
#     down = num
    
#     while up < 10 or down > -1:
#         up += 1
#         down -= 1
#         if up < 10 and error_num[up]:
#             return temp + str(up)
#         if down > -1 and error_num[down]:
#             return temp + str(down)

# def channer(N):
#     two_button_cnt = 0
#     all_button_cnt = 0
#     temp = ""
    
#     if N <= 100:
#         two_button_cnt = 100 - N
#     elif N > 100:
#         two_button_cnt = N - 100

#     for num in str(N):
#         num = int(num)
#         if error_num[num]:
#             all_button_cnt += 1
#             temp += str(num)
#         else:
#             all_button_cnt += 1
#             temp = min_num(temp, num)

#     if temp == None:
#         all_button_cnt = inf
#     elif N > int(temp):
#         all_button_cnt += N - int(temp)
#     else:
#         all_button_cnt += int(temp) - N
    
#     print(min(two_button_cnt, all_button_cnt))

# N, M = int(input()), int(input())
# error_num = [True] * 10
# for num in (map(int, input().split())):
#     error_num[num] = False

# channer(N)

# # 2차 시도 - 참고 https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-1107-%EB%A6%AC%EB%AA%A8%EC%BB%A8
# target = int(input())
# ans = abs(100 - target) # ++ or -- 로 이동할 경우 -> 최댓값
# M = int(input())
# if M: # 고장난게 있을 경우만 인풋을 받음
#     broken = set(input().split())
# else:
#     broken = set()

# # 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# # 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
# for num in range(1000001): 
#     for N in str(num):
#         if N in broken: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
#             break
#     else: # 번호를 눌러서 만들 수 있는 경우엔
#     	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)

#         ans = min(ans, len(str(num)) + abs(num - target))
# print(ans)

# 3차 시도
from sys import stdin
input = stdin.readline

N, M = int(input()), int(input())
if M:
    error_num = list(map(int, input().split()))
else:
    error_num = list()

ans = abs(N - 100)

for num in range(1000001):
    if len(str(num)) > len(str(N))+1:
        break

    ck = True
    for ck_num in str(num):
        if int(ck_num) in error_num:
            ck = False
            break
    if ck:
        ans = min(ans, len(str(num)) + abs(N-num))

print(ans)