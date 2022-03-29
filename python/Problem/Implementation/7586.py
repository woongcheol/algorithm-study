from sys import stdin
input = stdin.readline

def ck_ranking(weight_lst):
    for i in range(N):
        cnt = 1
        for j in range(N):
            if i == j:
                continue
            else:
                a, b = weight_lst[i]
                c, d = weight_lst[j]

                if a < c and b < d:
                    cnt += 1
                else:
                    continue
        print(cnt, end = " ")

N = int(input())
weight_lst = list()

for _ in range(N):
    weight, height = map(int, input().split())
    weight_lst.append((weight, height))

ck_ranking(weight_lst)