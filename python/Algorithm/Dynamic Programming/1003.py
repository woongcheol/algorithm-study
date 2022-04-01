from sys import stdin

input = stdin.readline

def fibonacci(num):
    if num == 0:
        print(zero_one[0][0], zero_one[0][1])
        return
    elif num == 1:
        print(zero_one[1][0], zero_one[1][1])
        return
    
    for idx in range(2, num+1):
        zero_one[idx][0] = zero_one[idx-1][0] + zero_one[idx-2][0]
        zero_one[idx][1] = zero_one[idx-1][1] + zero_one[idx-2][1]

    print(zero_one[num][0], zero_one[num][1])

T = int(input())

zero_one = [[0, 0] for _ in range(41)]

# 0일때
zero_one[0][0] = 1
zero_one[0][1] = 0

# 1일때
zero_one[1][0] = 0
zero_one[1][1] = 1

for _ in range(T):
    num = int(input())
    fibonacci(num)