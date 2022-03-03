# 개인 풀이
n = int(input())
b_lst = list(map(int, input().split()))
a_lst = list()

for i in range(len(b_lst)):
    num = b_lst[i] * (i+1)
    for j in range(i):
        num -= a_lst[j]
    a_lst.append(num)

for num in a_lst:
    print(num, end=' ')

# 강의 풀이
n, b_lst = int(input()), list(map(int, input().split()))
a_lst = [b_lst[0]]

for i in range(1, n):
    a_lst.append(b_lst[i]*(i+1) - sum(a_lst))

for num in a_lst:
    print(num, end=' ')

# 강의 풀이 2
n, b_lst = int(input()), list(map(int, input().split()))
a_lst = [0 for i in range(n)]
a_lst[0] = b_lst[0]

for i in range(1, n):
    a_lst[i] = b_lst[i]*(i+1) - sum(a_lst)

for num in a_lst:
    print(num, end=' ')