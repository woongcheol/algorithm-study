from collections import deque

N, K = map(int, input().split())

people = deque([i for i in range(1, N+1)])
cnt = 0

print('<', end = "")
while people:
    cnt += 1
    num = people.popleft()
    if len(people) == 0:
        print(f'{num}>')
    elif cnt % K == 0:
        print(f'{num},', end = ' ')
    else:
        people.append(num)