from sys import stdin
input = stdin.readline
N = int(input())
point_lst = []
for idx in range(N):
    x, y = map(int, input().split())
    point_lst.append((y, x))

point_lst.sort()
for y, x in point_lst:
    print(x, y)