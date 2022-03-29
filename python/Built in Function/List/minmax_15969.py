# 백준 - https://www.acmicpc.net/problem/15969

N, lst = int(input()), list(map(int, input().split()))

print(max(lst)-min(lst))