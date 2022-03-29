import sys

N = int(input())
number_list = [0]*10001
for idx in range(N):
    num = int(sys.stdin.readline())
    number_list[num] += 1

for idx2 in range(len(number_list)):
    check = number_list[idx2]
    while check:
        print(idx2)
        check -= 1