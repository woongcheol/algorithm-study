# 1차 시도
# # def top(number):

#     # 벽돌 생성
#     block_array = list()
#     for idx in range(1, number+1):
#         width, height, weight = map(int, input().split())
#         block_array.append((width, height, weight, idx))
#     s_block = sorted(block_array)
    
#     # dp 적용
#     dp = [[0] * (number+1) for _ in range(number+1)]

#     for i in range(1, number+1):
#         for j in range(1, number+1):
#             if s_block[i-1][0] == s_block[j-1][0]:
#                 dp[i][j] = max(dp[i-1][j], s_block[i-1][1])
#                 continue
#             elif s_block[i-1][0] > s_block[j-1][0]:
#                 dp[i][j] = max(dp[i-1][j], s_block[i-1][1] + s_block[j-1][1]) 
#                 continue
#             elif s_block[i-1][0] < s_block[j-1][0]:
#                 if s_block[i-1][2] < s_block[j-1][2]:
#                     dp[i][j] = max(dp[i-1][j] + s_block[i-1][1], s_block[j-1][1] + s_block[i-1][1])
#                 else:
#                     dp[i][j] = dp[i-1][j]

#     max_1 = 0
#     cnt = 0
#     result = list()
    
#     for i in range(1, number+1):
#         if max_1 < dp[-1][i]:
#             max_1 = dp[-1][i]

#     for i in range(number, -1, -1):
#         if dp[-1][i] == max_1:
#             for j in range(number):
#                 if dp[j][5] != dp[j+1][5]:
#                     result.append(s_block[j][3])
#                     cnt += 1
#             result.append(s_block[i-1][3])
#             cnt += 1

#     print(cnt)
    
#     for data in result:
#         print(data)
                
# N = int(input())
# top(N)

# 2차 시도
def block(N):
    array = []

    array.append((0, 0, 0, 0))
    for i in range(1, N+1):
        area, height, weight = map(int, input().split())
        array.append((i, area, height, weight))

    # 무게를 기준으로 정렬
    array.sort(key=lambda x:x[3])

    dp = [0] * (N + 1)

    for i in range(1, N+1):
        for j in range(0, i):
            if array[i][1] > array[j][1]:
                dp[i] = max(dp[i], dp[j] + array[i][2])
    
    max_value = max(dp)
    index = N
    result = list()

    while index != 0:
        if max_value == dp[index]:
            result.append(array[index][0])
            max_value -= array[index][2]
        index -= 1

    result.reverse()
    print(len(result))
    [print(i) for i in result]

N = int(input())
block(N)

