from sys import stdin
input = stdin.readline

K = int(input())
num_list = list()
res = 0
cnt = 0

for _ in range(K):
    num = int(input())
    
    if not num:
        res -= num_list[-1]
        num_list.pop()
    else:
        num_list.append(num)
        res += num

print(res)