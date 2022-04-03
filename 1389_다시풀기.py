# 1차 시도
# from cmath import inf
# from sys import stdin

# input = stdin.readline

# N, M = map(int, input().split())
# friends = [set() for _ in range(N+1)]
# for _ in range(M):
#     person, friend = map(int, input().split())
#     friends[person].add(friend)
#     friends[friend].add(person)

# max_num = 0
# min_person = 5000
# for idx in range(1, len(friends)):
#     if max_num <= len(friends[idx]):
#         if max_num == len(friends[idx]):
#             min_person = min(min_person, idx)
#             continue
#         max_num = len(friends[idx])
#         min_person = idx        

# print(min_person)

# 2차 시도
# from cmath import inf
from collections import deque
from sys import stdin

input = stdin.readline

def bfs(num, N):
    bacon = [0]*(N+1)
    visited = [num]
    queue = deque()
    queue.append(num)

    while queue:
        k = queue.popleft()
        for i in friends[k]:
            if i not in visited:
                bacon[i] = bacon[k] + 1
                visited.append(i)
                queue.append(i)
    return sum(bacon)

N, M = map(int, input().split())
friends = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)

print(friends)

result = []
for num in range(1, N+1):
    result.append(bfs(num, N))

print(result)

print(result.index(min(result))+1)